class MyList(list):
    def print_sorted(self):
        new = self[:]
        new.sort()
        print(new)
