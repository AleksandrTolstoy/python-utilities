from decimal import Decimal, ROUND_HALF_UP

def super_range(start, stop, step):
    """Advance range with float numbers support"""
    start, stop, step = Decimal(start), Decimal(stop), Decimal(step)
    while start < stop:
        yield start.quantize(Decimal("1.00"), ROUND_HALF_UP).__float__()
        start += step

if __name__ == '__main__':
    print(list(super_range(1, 5, 0.2)))
