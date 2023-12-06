    def init_veggies(self):
        filename = input("Enter veggie file name: ")
        while not os.path.exists(filename):
            print("File not found")
            filename = input("Enter veggie file name: ")

        with open(filename) as f:
            lines = f.readlines()
            first_line = lines[0]
            dimensions = first_line.strip().split(',')
            self.height = int(dimensions[1])
            self.width = int(dimensions[2])
            # height, width = [int(x) for x in lines[0].strip().split(',')]
            self._field = [[None for _ in range(self.width)] for _ in range(self.height)]

            for line in lines[1:]:
                data = line.strip().split(',')
                veggie = Veggie(data[0], data[1], int(data[2]))
                self._veggies.append(veggie)

        for _ in range(self.NUMBER_VEGGIES):
            occupied = True
            while occupied:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if not self._field[y][x]:
                    self._field[y][x] = random.choice(self._veggies)
                    occupied = False

    def init_captain(self):
        occupied = True
        while occupied:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self._field[y][x]:
                self._captain = Captain(x,y)
                self._field[y][x] = self._captain
                occupied = False


    def init_rabbits(self):
        for _ in range(self.NUMBER_RABBITS):
            occupied = True
            while occupied:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if not self._field[y][x]:
                    rabbit = Rabbit(x, y)
                    self._rabbits.append(rabbit)
                    self._field[y][x] = rabbit
                    occupied = False