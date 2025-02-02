import random
import math

# Функция активации (ReLU)
def relu(x):
    return max(0, x)

# Производная ReLU
def relu_derivative(x):
    return 1 if x > 0 else 0

# Создание нейросети с одним скрытым слоем
class NeuralNetwork:
    def __init__(self):
        # Инициализация весов
        self.input_weights = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(5)]  # 2 входа -> 5 нейронов
        self.hidden_biases = [random.uniform(-1, 1) for _ in range(5)]
        self.hidden_weights = [random.uniform(-1, 1) for _ in range(5)]  # 5 скрытых -> 1 выход
        self.output_bias = random.uniform(-1, 1)

    def forward(self, inputs):
        # Вычисление скрытого слоя
        hidden_outputs = [relu(sum(w * i for w, i in zip(weights, inputs)) + b) 
                          for weights, b in zip(self.input_weights, self.hidden_biases)]
        # Вычисление выходного слоя
        total = sum(w * h for w, h in zip(self.hidden_weights, hidden_outputs)) + self.output_bias
        return relu(total)

    def train(self, training_data, learning_rate=0.01, epochs=10000):
        for _ in range(epochs):
            x, y = random.choice(training_data)
            target = x + y
            
            # Прямой проход
            hidden_outputs = [relu(sum(w * i for w, i in zip(weights, [x, y])) + b) 
                              for weights, b in zip(self.input_weights, self.hidden_biases)]
            output = sum(w * h for w, h in zip(self.hidden_weights, hidden_outputs)) + self.output_bias
            
            # Ошибка и корректировка весов выходного слоя
            error = target - output
            output_adjustment = error * relu_derivative(output)
            self.hidden_weights = [w + learning_rate * output_adjustment * h 
                                   for w, h in zip(self.hidden_weights, hidden_outputs)]
            self.output_bias += learning_rate * output_adjustment
            
            # Корректировка весов скрытого слоя
            hidden_adjustments = [output_adjustment * w * relu_derivative(h) 
                                  for w, h in zip(self.hidden_weights, hidden_outputs)]
            for i in range(5):
                self.input_weights[i] = [w + learning_rate * hidden_adjustments[i] * inp 
                                         for w, inp in zip(self.input_weights[i], [x, y])]
                self.hidden_biases[i] += learning_rate * hidden_adjustments[i]

# Генерация тренировочных данных
training_data = [(x, y) for x in range(1, 10) for y in range(1, 10)]
nn = NeuralNetwork()

# Обучение сети
nn.train(training_data)

# Проверка результата
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} + {y} ≈ {nn.forward([x, y]):.1f}")
