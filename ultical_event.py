from ics import Event, Geo
import itertools

divisions_enum = {
    1: 'Mixed',
    2: 'Open',
    3: 'Women',
    4: 'Masters',
    5: 'Youth',
    6: 'Loose Mixed'
}

level_enum = {
    1: 'Beginner',
    2: 'Intermediate',
    3: 'Advanced'
}

field_type_enum = {
    1: 'Beach',
    2: 'Grass',
    3: 'Indoor'
}

organizer_type_enum = {
    1: 'Independent',
    2: 'Federation',
}

team_format_enum = {
    1: '4 vs. 4',
    2: '5 vs. 5',
    3: '6 vs. 6',
    4: '7 vs. 7'
}

event_type_enum = {
    1: 'Tournament',
    2: 'HAT tournament',
    3: 'Pick-up',
    4: 'Competition',
    5: 'Try-out',
    6: 'Training',
    7: 'Clinic',
    8: 'Camp',
    9: 'Championship',
}


class UlticalEvent:
    def __init__(self, data):
        self.id = data.get('Id')
        self.name = data.get('Name')
        self.description = data.get('Description')
        self.edition = data.get('Edition')
        self.number_of_teams = data.get('NumberOfTeams')
        self.organizer = data.get('Organizer')
        self.verified = data.get('Verified')
        self.latitude = float(data.get('Lat'))
        self.longitude = float(data.get('Lng'))
        self.year = data.get('Year')
        self.start_date = data.get('StartDate')
        self.end_date = data.get('EndDate')
        self.street = data.get('Street')
        self.city = data.get('City')
        self.country = data.get('Country')
        self.country_abbreviation = data.get('CountryAbr')
        self.cancelled = data.get('Cancelled')
        self.website = data.get('Website')
        self.youtube_url = data.get('YoutubeUrl')
        self.registration_url = data.get('RegistrationUrl')
        self.file_name = data.get('FileName')
        self.divisions = list(
            map(divisions_enum.get, data.get('Filter').get('Division') if data.get('Filter').get('Division') else []))
        self.levels = list(
            map(level_enum.get, data.get('Filter').get('Level') if data.get('Filter').get('Level') else []))
        self.field_types = list(map(field_type_enum.get,
                                    data.get('Filter').get('FieldType') if data.get('Filter').get('FieldType') else []))
        self.team_formats = list(map(team_format_enum.get,
                                     data.get('Filter').get('TeamFormat') if data.get('Filter').get(
                                         'TeamFormat') else []))
        self.event_types = list(map(event_type_enum.get,
                                    data.get('Filter').get('EventType') if data.get('Filter').get('EventType') else []))
        self.organizer_type = list(
            map(organizer_type_enum.get,
                data.get('Filter').get('Organizer') if data.get('Filter').get('Organizer') else []))[0]

    def to_ics_event(self) -> Event:
        e = Event()
        e.name = self.name
        e.begin = self.start_date
        e.end = self.end_date
        e.organizer = self.organizer
        e.geo = Geo(self.latitude, self.longitude)
        e.location = f'{self.country}, {self.city}'
        description_header = '\n'.join(
            list(itertools.chain.from_iterable([self.levels, self.divisions, self.field_types, self.team_formats])))
        e.description = f'{description_header}\n\n{self.description}'
        e.url = self.registration_url
        e.categories = list(itertools.chain.from_iterable([self.levels, self.divisions, self.field_types,
                                                           self.team_formats]))
        e.make_all_day()
        return e


def __str__(self):
    return f"UlticalEvent: {self.name} ({self.start_date} - {self.end_date})"


def __repr__(self):
    return f"UlticatEvent(name='{self.name}', start_date='{self.start_date}', end_date='{self.end_date}')"
