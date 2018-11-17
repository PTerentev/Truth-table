

class MyMath:

    def __init__(self, string, variables):
        self.string = str(string)
        self.count = len(variables)
        self.variables = list()
        for var in variables:
            self.variables.append(var)
        if self.count == 1:
            self.table = self.MakingTable1()
        elif self.count == 2:
            self.table = self.MakingTable2()
        elif self.count == 3:
            self.table = self.MakingTable3()
        elif self.count == 4:
            self.table = self.MakingTable4()
        self.values = self.Math()


    def Print(self):

        string = str()
        for var in self.variables:
            string += " " + str(var)
        string += " "*2 + self.string + "\n"
        for attrs in self.table:
            for attr in self.table[attrs]:
                string += " " + str(attr)
            string += " "*2 + str(self.values[int(attrs)]) + "\n"
        return string

    def Math(self):
        values = list()
        string = str(self.string)
        string = string.replace("+", " or ")
        string = string.replace("*", " and ")
        string = string.replace("not", " not ")
        for number in self.table:
            mathString = str(string)
            attrs = self.table[str(number)]
            for i in range(len(attrs)):
                if attrs[i] == 0:
                    mathString = mathString.replace(self.variables[i], "False")
                else:
                    mathString = mathString.replace(self.variables[i], "True")

            if eval(mathString, {'__builtins__':{}}) == True:
                values.append("1")
            else:
                values.append("0")


        return values




    def MakingTable1(self):
        table = dict()
        attr = list()
        count = 0
        for i in range(2):
            attr.append(i)
            table.update({str(count): list(attr)})
            count += 1
            attr.clear()
        return table

    def MakingTable2(self):
        table = dict()
        attr = list()
        count = 0
        for i in range(2):
            for j in range(2):
                attr.append(i)
                attr.append(j)
                table.update({str(count): list(attr)})
                count += 1
                attr.clear()
        return table

    def MakingTable3(self):
        table = dict()
        attr = list()
        count = 0
        for i in range(2):
            for j in range(2):
                for m in range(2):
                    attr.append(i)
                    attr.append(j)
                    attr.append(m)
                    table.update({str(count): list(attr)})
                    count += 1
                    attr.clear()

        return table

    def MakingTable4(self):
        table = dict()
        attr = list()
        count = 0
        for i in range(2):
            for j in range(2):
                for m in range(2):
                    for k in range(2):
                        attr.append(i)
                        attr.append(j)
                        attr.append(m)
                        attr.append(k)
                        table.update({str(count): list(attr)})
                        count += 1
                        attr.clear()
        return table


test = MyMath("notX*notY+Z+Y*X", "XYZ")
print(test.Print())
