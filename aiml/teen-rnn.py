input = [
    [ 1 , 1 , 1 ],
    [ 2 , 3 , 5 , 2 , 1 ],
    [ 1 ],
    [ 5 , 2 , 1 , 5 ],
]



output = [
    3,
    13,
    1,
    13
]


class RNN:
    def __init__(self,iweight,hweight,oweight):
        self.iweight = iweight
        self.hweight = hweight
        self.oweight = oweight
        self.h = 0
    def predict(self,features,labels):
        for row , label in zip(features,labels):
            self.h = 0
            output = None
            for unit in row:
                self.h = self.iweight * unit + self.hweight * self.h
                output = self.h * self.oweight
            error = output - label
            print('Input %s , Expected: %s , Got %s ' % (row,label,output))
    def train(input, output):
        for row , label in zip(features , labels):
        



model = RNN(0,0,0)
model.predict(input,output)
