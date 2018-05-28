#!/usr/local/bin/python3


def find_score_combinations(target, individual_scores):
    target_combinations_cache = [[1] + [0] * target for s in individual_scores]
    for i in range(len(individual_scores)):
        for j in range(1, target + 1):
            j_combs_without_score_i = target_combinations_cache[i-1][j] if i >= 1 else 0
            j_combs_with_score_i = target_combinations_cache[i][j - individual_scores[i]] if j >= individual_scores[i] else 0

            target_combinations_cache[i][j] = j_combs_without_score_i + j_combs_with_score_i

    for row in target_combinations_cache:
        print(row)
    return target_combinations_cache[-1][-1]


if __name__ == '__main__':
    print('Find several individual play score combinations for a final score!')

    print("find_score_combinations(target: {}, individual_scores: {}) -> {}".format(12, [2, 3, 7], find_score_combinations(12, [2, 3, 7])))
