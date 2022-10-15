class Musician:

    def __init__(self, name='Random Musician'):
        self.name = name


class Band(Musician):

    def __init__(self, band='Random Band'):
        self.name = band

        if band_name(self.band_name == {nirvana} not in '[]'):
            print(band_name, [])
        else:
            return []
        # if nirvana == band_name:
        #     return "Nirvana"
        # else:
        #     return []

    def get_instrument(self):
        return f'{self.name}'

    def __str__(self):
        return


class Bassist(Musician):

    def __init__(self, name='Random Bassist'):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'


class Drummer(Musician):

    def __init__(self, name='Random Drummer'):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


class Guitarist(Musician):

    def __init__(self, name='Random Guitarist'):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


if __name__ == '__main__':
    members = []
    joan = Guitarist("Joan Jett")
    members.append(joan)
    print(joan.__repr__())
    sheila = Drummer("Sheila E.")
    members.append(sheila)
    print(sheila.__repr__())
    meshell = Bassist("Meshell Ndegeocello")
    members.append(meshell)
    print(meshell.__repr__())
    jimi = Guitarist("Jimi Hendrix")
    members.append(jimi)
    print(jimi.__repr__())
    band_name = []
    the_nobodies = Band(["The Nobodies"])
    band_name.append(the_nobodies)
    nirvana = Band(["Nirvana"])
    band_name.append(nirvana)
    print(band_name)
