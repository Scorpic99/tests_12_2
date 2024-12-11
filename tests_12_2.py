import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers

class RunnerTest(unittest.TestCase):
    speed = 0

    def test_walk(self):
        runer = Runner('<NAME>')
        for i in range(10):
            runer.walk()
        self.assertEqual(runer.distance, 50)

    def test_run(self):
        runer = Runner('<NAME>')
        for i in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    def test_challenger(self):
        runner1 = Runner('<NAME>')
        runner2 = Runner('<NAME>')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
    def setUp(self):
        self.obj_runer1 = Runner('Усэйн', 10)
        self.obj_runer2 = Runner('Андрей', 9)
        self.obj_runer3 = Runner('Ник', 3)

    def test_dif_runers1(self):
        tournament = Tournament(90, self.obj_runer1, self.obj_runer3)
        finishers = tournament.start()
        self.all_results.append(finishers)
        self.assertTrue(finishers[max(finishers)], 'Ник')
    def test_dif_runers2(self):
        tournament = Tournament(90, self.obj_runer2, self.obj_runer3)
        finishers = tournament.start()
        self.all_results.append(finishers)
        self.assertTrue(finishers[max(finishers)], 'Ник')
    def test_dif_runers3(self):
        tournament = Tournament(90, self.obj_runer1, self.obj_runer2, self.obj_runer3)
        finishers = tournament.start()
        self.all_results.append(finishers)
        self.assertTrue(finishers[max(finishers)], 'Ник')
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)


TT = TournamentTest()