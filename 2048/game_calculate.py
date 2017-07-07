class GameCalculate:
    def __init__(self, item_data):
        self.data = item_data

    def calculate(self, direction):
        if len(self.data) <= 0:
            return 0
        if direction == 1:
            self.up_run()
        if direction == 2:
            self.down_run()
        if direction == 3:
            self.left_run()
        if direction == 4:
            self.right_run()

    def get_data(self):
        return self.data

    def up_run(self):
        for i in range(0, 4):
            k = None
            for j in range(0, 4):
                l = self.data[j][i]
                if k and l["Number"] != 0:
                    k_v = self.data[k["j"]][k["i"]]
                    if k_v["Number"] == l["Number"]:
                        self.data[k["j"]][k["i"]]["Number"] = k_v["Number"] + l["Number"]
                        self.data[j][i] = {"Item": None, "Number": 0}
                        k = None
                    else:
                        if l["Number"] != 0: k = {"i": i, "j": j}
                else:
                    k = {"i": i, "j": j}
        for i in range(0, 4):
            for j in range(0, 4):
                if self.data[j][i]["Number"] != 0:
                    if j != 0:
                        for k in range(0, j):
                            if self.data[k][i]["Number"] == 0:
                                swap = self.data[k][i]
                                self.data[k][i] = self.data[j][i]
                                self.data[j][i] = swap
                                break

    def down_run(self):
        for i in range(0, 4):
            k = None
            for j in range(3, -1, -1):
                l = self.data[j][i]
                if k and l["Number"] != 0:
                    k_v = self.data[k["j"]][k["i"]]
                    if k_v["Number"] == l["Number"]:
                        self.data[k["j"]][k["i"]]["Number"] = k_v["Number"] + l["Number"]
                        self.data[j][i] = {"Item": None, "Number": 0}
                        k = None
                    else:
                        k = {"i": i, "j": j}
                else:
                    if l["Number"] != 0: k = {"i": i, "j": j}

        for i in range(0, 4):
            for j in range(0, 4):
                if self.data[3 - j][i]["Number"] != 0:
                    if 3 - j != 3:
                        for k in range(3, 3 - j - 1, -1):
                            if self.data[k][i]["Number"] == 0:
                                swap = self.data[k][i]
                                self.data[k][i] = self.data[3 - j][i]
                                self.data[3 - j][i] = swap
                                break

    def left_run(self):
        for i in range(0, 4):
            k = None
            for j in range(0, 4):
                l = self.data[i][j]
                if k and l["Number"] != 0:
                    k_v = self.data[k["i"]][k["j"]]
                    if k_v["Number"] == l["Number"]:
                        self.data[k["i"]][k["j"]]["Number"] = k_v["Number"] + l["Number"]
                        self.data[i][j] = {"Item": None, "Number": 0}
                        k = None
                    else:
                        k = {"i": i, "j": j}
                else:
                    if l["Number"] != 0: k = {"i": i, "j": j}
        for i in range(0, 4):
            for j in range(0, 4):
                if self.data[i][j]["Number"] != 0:
                    if j != 0:
                        for k in range(0, j):
                            if self.data[i][k]["Number"] == 0:
                                swap = self.data[i][k]
                                self.data[i][k] = self.data[i][j]
                                self.data[i][j] = swap
                                break

    def right_run(self):
        for i in range(0, 4):
            k = None
            for j in range(3, -1, -1):
                l = self.data[i][j]
                if k and l["Number"] != 0:
                    k_v = self.data[k["i"]][k["j"]]
                    if k_v["Number"] == l["Number"]:
                        self.data[k["i"]][k["j"]]["Number"] = k_v["Number"] + l["Number"]
                        self.data[i][j] = {"Item": None, "Number": 0}
                        k = None
                    else:
                        k = {"i": i, "j": j}
                else:
                    if l["Number"] != 0: k = {"i": i, "j": j}
        for i in range(0, 4):
            for j in range(0, 4):
                if self.data[i][3 - j]["Number"] != 0:
                    if 3 - j != 3:
                        for k in range(3, 3 - j - 1, -1):
                            if self.data[i][k]["Number"] == 0:
                                swap = self.data[i][k]
                                self.data[i][k] = self.data[i][3 - j]
                                self.data[i][3 - j] = swap
                                break
