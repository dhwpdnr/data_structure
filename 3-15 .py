class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def degree(self):
        return len(self.coefficients) - 1

    def evaluate(self, scalar):
        return sum(coef * (scalar ** idx) for idx, coef in enumerate(self.coefficients))

    def add(self, rhs):
        max_len = max(len(self.coefficients), len(rhs.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            a_coef = self.coefficients[i] if i < len(self.coefficients) else 0
            b_coef = rhs.coefficients[i] if i < len(rhs.coefficients) else 0
            result[i] = a_coef + b_coef
        return Polynomial(result)

    def subtract(self, rhs):
        max_len = max(len(self.coefficients), len(rhs.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            a_coef = self.coefficients[i] if i < len(self.coefficients) else 0
            b_coef = rhs.coefficients[i] if i < len(rhs.coefficients) else 0
            result[i] = a_coef - b_coef
        return Polynomial(result)

    def multiply(self, rhs):
        result = [0] * (len(self.coefficients) + len(rhs.coefficients) - 1)
        for self_idx, self_coef in enumerate(self.coefficients):
            for rhs_idx, rhs_coef in enumerate(rhs.coefficients):
                result[self_idx + rhs_idx] += self_coef * rhs_coef
        return Polynomial(result)

    def display(self, prefix=""):
        terms = []
        for idx, coef in enumerate(reversed(self.coefficients)):
            power = len(self.coefficients) - idx - 1
            if coef != 0:
                if power == 0:
                    terms.append(f"{coef}")
                elif power == 1:
                    terms.append(f"{coef} x")
                else:
                    terms.append(f"{coef} x^{power}")
        formatted_terms = ' + '.join(terms).replace('+ -', '- ')
        print(prefix + formatted_terms)


def read_poly():
    degree = int(input("다항식의 최고 차수를 입력하시오: "))
    coefficients = []
    for i in range(degree, -1, -1):
        coef = float(input(f"x^{i}의 계수: "))
        coefficients.append(coef)
    return Polynomial(coefficients[::-1])


# 사용 예시
a = read_poly()
b = read_poly()
c = a.add(b)
c.display("a + b = ")
c = a.subtract(b)
c.display("a - b = ")
c = a.multiply(b)
c.display("a * b = ")
print(f"a(2) = {a.evaluate(2)}")
print(f"b(2) = {b.evaluate(2)}")
print(f"c(2) = {c.evaluate(2)}")
print(f"degree of a: {a.degree()}")
print(f"degree of b: {b.degree()}")
print(f"degree of c: {c.degree()}")
