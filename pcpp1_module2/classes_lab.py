class Luxe_Watch():
    _luxe_watches_created = 0
    
    def __init__(self):
        Luxe_Watch._luxe_watches_created += 1
        self.engraving_text = ''
        print("\nNew luxe watch created.")
    
    @classmethod
    def luxe_with_engraving(cls, engraving_text):
        if Luxe_Watch.engraving_text_is_valid(engraving_text):
            _watch = cls()
            _watch.engraving_text = engraving_text
            print("New luxe watch created with engraving:", engraving_text)
        else:
            raise Exception
        return _watch
    
    @classmethod
    def get_number_of_watches_created(cls):
        return cls._luxe_watches_created
    
    @staticmethod
    def engraving_text_is_valid(engraving_text):
        if len(engraving_text)>40 or not engraving_text.isalpha():
            return False
        else:
            return True

watch1 = Luxe_Watch()
print("Number of luxe watches created:", Luxe_Watch.get_number_of_watches_created())

watch2 = Luxe_Watch.luxe_with_engraving('LuxuryWatchCo')
print("Number of luxe watches created:", Luxe_Watch.get_number_of_watches_created())

try:
    watch3 = Luxe_Watch.luxe_with_engraving('foo@baz.com')
except:
    print('The engraving text is not correct for your watch.')
print("Number of luxe watches created:", Luxe_Watch.get_number_of_watches_created())