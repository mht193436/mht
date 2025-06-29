# 练习题1：定义一个 Car 类
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        self.speed += m * 10

    def brake(self, n):
        self.speed -= n * 10
        if self.speed < 0:
            self.speed = 0

# 练习题2：创建 Car 类的实例，调用加速和刹车方法，输出当前速度
my_car = Car("Toyota")
print(f"Initial speed: {my_car.speed}")  # 输出: Initial speed: 0

my_car.accelerate(3)
print(f"Speed after accelerating 3 times: {my_car.speed}")  # 输出: Speed after accelerating 3 times: 30

my_car.brake(1)
print(f"Speed after braking 1 time: {my_car.speed}")  # 输出: Speed after braking 1 time: 20

my_car.brake(5)
print(f"Speed after braking 5 times: {my_car.speed}")  # 输出: Speed after braking 5 times: 0

# 练习题3：定义 ElectricCar 子类继承 Car
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=0):
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self):
        self.battery += 20
        if self.battery > 100:
            self.battery = 100

# 创建 ElectricCar 类的实例，调用加速、刹车和充电方法，输出当前速度和电量
my_electric_car = ElectricCar("Tesla", battery=80)
print(f"Initial speed: {my_electric_car.speed}, Battery: {my_electric_car.battery}")  # 输出: Initial speed: 0, Battery: 80

my_electric_car.accelerate(2)
print(f"Speed after accelerating 2 times: {my_electric_car.speed}, Battery: {my_electric_car.battery}")  # 输出: Speed after accelerating 2 times: 20, Battery: 80

my_electric_car.brake(1)
print(f"Speed after braking 1 time: {my_electric_car.speed}, Battery: {my_electric_car.battery}")  # 输出: Speed after braking 1 time: 10, Battery: 80

my_electric_car.charge()
print(f"Speed after charging: {my_electric_car.speed}, Battery: {my_electric_car.battery}")  # 输出: Speed after charging: 10, Battery: 100

my_electric_car.charge()
print(f"Speed after charging again: {my_electric_car.speed}, Battery: {my_electric_car.battery}")  # 输出: Speed after charging again: 10, Battery: 100