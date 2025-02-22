# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import retworkx


class TestIsomorphic(unittest.TestCase):
    def test_empty_isomorphic_identical(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(g_a, g_b, id_order=id_order)
                )

    def test_empty_isomorphic(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(g_a, g_b, id_order=id_order)
                )

    def test_empty_isomorphic_compare_nodes(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_isomorphic_identical(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["a_1", "a_2", "a_3"])
        g_b.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(g_a, g_b, id_order=id_order)
                )

    def test_isomorphic_mismatch_node_data(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["b_1", "b_2", "b_3"])
        g_b.add_edges_from(
            [(nodes[0], nodes[1], "b_1"), (nodes[1], nodes[2], "b_2")]
        )
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(g_a, g_b, id_order=id_order)
                )

    def test_isomorphic_compare_nodes_mismatch_node_data(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["b_1", "b_2", "b_3"])
        g_b.add_edges_from(
            [(nodes[0], nodes[1], "b_1"), (nodes[1], nodes[2], "b_2")]
        )
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertFalse(
                    retworkx.is_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_is_isomorphic_nodes_compare_raises(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["b_1", "b_2", "b_3"])
        g_b.add_edges_from(
            [(nodes[0], nodes[1], "b_1"), (nodes[1], nodes[2], "b_2")]
        )

        def compare_nodes(a, b):
            raise TypeError("Failure")

        self.assertRaises(
            TypeError, retworkx.is_isomorphic, (g_a, g_b, compare_nodes)
        )

    def test_isomorphic_compare_nodes_identical(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["a_1", "a_2", "a_3"])
        g_b.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_isomorphic_compare_edges_identical(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["a_1", "a_2", "a_3"])
        g_b.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(
                        g_a,
                        g_b,
                        edge_matcher=lambda x, y: x == y,
                        id_order=id_order,
                    )
                )

    def test_isomorphic_removed_nodes_in_second_graph(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from(
            [(nodes[0], nodes[1], "a_1"), (nodes[1], nodes[2], "a_2")]
        )

        nodes = g_b.add_nodes_from(["a_0", "a_2", "a_1", "a_3"])
        g_b.add_edges_from(
            [
                (nodes[0], nodes[1], "e_01"),
                (nodes[0], nodes[3], "e_03"),
                (nodes[2], nodes[1], "a_1"),
                (nodes[1], nodes[3], "a_2"),
            ]
        )
        g_b.remove_node(nodes[0])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertTrue(
                    retworkx.is_isomorphic(
                        g_a, g_b, lambda x, y: x == y, id_order=id_order
                    )
                )

    def test_isomorphic_node_count_not_equal(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(["a_1", "a_2", "a_3"])
        g_a.add_edges_from([(nodes[0], nodes[1], "a_1")])

        nodes = g_b.add_nodes_from(["a_0", "a_1"])
        g_b.add_edges_from([(nodes[0], nodes[1], "a_1")])
        g_b.remove_node(nodes[0])
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertFalse(
                    retworkx.is_isomorphic(g_a, g_b, id_order=id_order)
                )

    def test_same_degrees_non_isomorphic(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()

        nodes = g_a.add_nodes_from(
            ["a_1", "a_2", "a_3", "a_4", "b_1", "b_2", "b_3", "b_4"]
        )
        g_a.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[2], nodes[3], "a_3"),
                (nodes[3], nodes[0], "a_4"),
                (nodes[4], nodes[5], "b_1"),
                (nodes[5], nodes[6], "b_2"),
                (nodes[6], nodes[7], "b_3"),
                (nodes[7], nodes[4], "b_4"),
                (nodes[0], nodes[4], "e_1"),
                (nodes[1], nodes[5], "e_2"),
            ]
        )

        nodes = g_b.add_nodes_from(
            ["a_1", "a_2", "a_3", "a_4", "b_1", "b_2", "b_3", "b_4"]
        )
        g_b.add_edges_from(
            [
                (nodes[0], nodes[1], "a_1"),
                (nodes[1], nodes[2], "a_2"),
                (nodes[2], nodes[3], "a_3"),
                (nodes[3], nodes[0], "a_4"),
                (nodes[4], nodes[5], "b_1"),
                (nodes[5], nodes[6], "b_2"),
                (nodes[6], nodes[7], "b_3"),
                (nodes[7], nodes[4], "b_4"),
                (nodes[0], nodes[4], "e_1"),
                (nodes[2], nodes[6], "e_2"),
            ]
        )
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                self.assertFalse(
                    retworkx.is_isomorphic(g_a, g_b, id_order=id_order)
                )

    def test_graph_isomorphic_self_loop(self):
        graph = retworkx.PyGraph()
        graph.add_nodes_from([0, 1])
        graph.add_edges_from_no_data([(0, 0), (0, 1)])
        self.assertTrue(retworkx.is_isomorphic(graph, graph))

    def test_isomorphic_parallel_edges(self):
        first = retworkx.PyGraph()
        first.extend_from_edge_list([(0, 1), (0, 1), (1, 2), (2, 3)])
        second = retworkx.PyGraph()
        second.extend_from_edge_list([(0, 1), (1, 2), (1, 2), (2, 3)])
        self.assertFalse(retworkx.is_isomorphic(first, second))

    def test_isomorphic_parallel_edges_with_edge_matcher(self):
        graph = retworkx.PyGraph()
        graph.extend_from_weighted_edge_list(
            [(0, 1, "a"), (0, 1, "b"), (1, 2, "c")]
        )
        self.assertTrue(
            retworkx.is_isomorphic(
                graph, graph, edge_matcher=lambda x, y: x == y
            )
        )

    def test_graph_isomorphic_insufficient_call_limit(self):
        graph = retworkx.generators.path_graph(5)
        self.assertFalse(retworkx.is_isomorphic(graph, graph, call_limit=2))

    def test_graph_vf2_mapping_identical(self):
        graph = retworkx.generators.grid_graph(2, 2)
        second_graph = retworkx.generators.grid_graph(2, 2)
        mapping = retworkx.graph_vf2_mapping(graph, second_graph)
        self.assertEqual(next(mapping), {0: 0, 1: 1, 2: 2, 3: 3})

    def test_graph_vf2_mapping_identical_removals(self):
        graph = retworkx.generators.path_graph(2)
        second_graph = retworkx.generators.path_graph(4)
        second_graph.remove_nodes_from([1, 2])
        second_graph.add_edge(0, 3, None)
        mapping = retworkx.graph_vf2_mapping(graph, second_graph)
        self.assertEqual({0: 0, 1: 3}, next(mapping))

    def test_graph_vf2_mapping_identical_removals_first(self):
        second_graph = retworkx.generators.path_graph(2)
        graph = retworkx.generators.path_graph(4)
        graph.remove_nodes_from([1, 2])
        graph.add_edge(0, 3, None)
        mapping = retworkx.graph_vf2_mapping(
            graph,
            second_graph,
        )
        self.assertEqual({0: 0, 3: 1}, next(mapping))

    def test_graph_vf2_mapping_identical_vf2pp(self):
        graph = retworkx.generators.grid_graph(2, 2)
        second_graph = retworkx.generators.grid_graph(2, 2)
        mapping = retworkx.graph_vf2_mapping(
            graph, second_graph, id_order=False
        )
        self.assertEqual(next(mapping), {0: 0, 1: 1, 2: 2, 3: 3})

    def test_graph_vf2_mapping_identical_removals_vf2pp(self):
        graph = retworkx.generators.path_graph(2)
        second_graph = retworkx.generators.path_graph(4)
        second_graph.remove_nodes_from([1, 2])
        second_graph.add_edge(0, 3, None)
        mapping = retworkx.graph_vf2_mapping(
            graph, second_graph, id_order=False
        )
        self.assertEqual({0: 0, 1: 3}, next(mapping))

    def test_graph_vf2_mapping_identical_removals_first_vf2pp(self):
        second_graph = retworkx.generators.path_graph(2)
        graph = retworkx.generators.path_graph(4)
        graph.remove_nodes_from([1, 2])
        graph.add_edge(0, 3, None)
        mapping = retworkx.graph_vf2_mapping(
            graph, second_graph, id_order=False
        )
        self.assertEqual({0: 0, 3: 1}, next(mapping))

    def test_graph_vf2_number_of_valid_mappings(self):
        graph = retworkx.generators.mesh_graph(3)
        mapping = retworkx.graph_vf2_mapping(graph, graph, id_order=True)
        total = 0
        for _ in mapping:
            total += 1
        self.assertEqual(total, 6)

    def test_empty_graph_vf2_mapping(self):
        g_a = retworkx.PyGraph()
        g_b = retworkx.PyGraph()
        for id_order in [False, True]:
            with self.subTest(id_order=id_order):
                mapping = retworkx.graph_vf2_mapping(
                    g_a, g_b, id_order=id_order, subgraph=False
                )
                self.assertEqual({}, next(mapping))
