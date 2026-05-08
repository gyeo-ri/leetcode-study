class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        def dfs(current: TreeNode | None):
            if not current:
                return

            left = current.left
            right = current.right
            current.right = left
            current.left = right

            dfs(current.right)
            dfs(current.left)

        dfs(root)
        return root


if __name__ == "__main__":
    from collections import deque

    def _build_tree(values: list[int | None]) -> TreeNode | None:
        if not values:
            return None

        nodes = [TreeNode(value) if value is not None else None for value in values]

        child_idx = 1

        for node in nodes:
            if node is not None:
                if child_idx < len(nodes):
                    node.left = nodes[child_idx]
                    child_idx += 1

                if child_idx < len(nodes):
                    node.right = nodes[child_idx]
                    child_idx += 1

        return nodes[0]

    def _tree_to_list(root: TreeNode | None) -> list[int | None]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                result.append(None)
                continue

            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while result and result[-1] is None:
            result.pop()

        return result

    test_cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, None, 2]),
    ]

    solution = Solution()

    for idx, (inp, expected) in enumerate(test_cases, start=1):
        root = _build_tree(inp)

        result_root = solution.invertTree(root)
        result = _tree_to_list(result_root)

        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"

    print("All test cases passed.")
