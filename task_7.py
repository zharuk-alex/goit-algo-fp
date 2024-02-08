import random
import matplotlib.pyplot as plt


def montecarlo_dices(dices=2, num_probs=10_000):
    temp_dict = {}

    for _ in range(num_probs):
        dices_sum = sum([random.randint(1, 6) for _ in range(dices)])
        temp_dict[dices_sum] = temp_dict.get(dices_sum, 0) + 1

    sorted_dict = dict(sorted(temp_dict.items()))
    result_dict = {
        key: round((value / num_probs) * 100, 2) for key, value in sorted_dict.items()
    }

    return result_dict


if __name__ == "__main__":
    num_dices = 2
    posible_combinations = 6**num_dices
    probability = montecarlo_dices(dices=num_dices, num_probs=10_000_000)

    print("\n")
    for key, value in probability.items():
        print(
            f"sum {key} : {value} ({round(value * posible_combinations / 100)}/{posible_combinations})"
        )
    print("\n")

    plt.figure(figsize=(10, 6))
    plt.bar(probability.keys(), probability.values(), color="skyblue")
    plt.xlabel("Points sum")
    plt.ylabel("Probability percentage")
    plt.title("Distribution of the sum of points when rolling two dice")
    plt.xticks(list(probability.keys()))
    plt.grid(axis="y")
    plt.show()
