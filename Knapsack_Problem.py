class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ':<' + str(self.value) + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    """
        names, values, calories lists of same length
        :param names: list of strings
        :param values: list of numbers
        :param calories: list of numbers
        :return: list of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu
