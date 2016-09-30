# -*- coding: utf-8 -*-
#
# test_weight_recorder.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""
Test of events
"""

import unittest
import nest
import numpy as np


@nest.check_stack
class WeightRecorderTestCase(unittest.TestCase):
    """Tests for the Weight Recorder"""

    def is_subset(self, a, b, places=6, msg=None):

        a = np.round(a, places)
        b = np.round(b, places)

        if set(a) <= set(b):
            return

        msg = self._formatMessage(msg, """List A is not subset of list B
                                  and/or the items are not equal within
                                  a certain range of precision.
                                  List A is {0} and list B is {1}"""
                                  .format(a, b))
        raise self.failureException(msg)

    def testSingleThread(self):
        """Weight Recorder Single Threaded"""

        nest.ResetKernel()
        nest.SetKernelStatus({"local_num_threads": 1})

        wr = nest.Create('weight_recorder')
        nest.CopyModel("stdp_synapse", "stdp_synapse_rec",
                       {"weight_recorder": wr[0], "weight": 1.})

        sg = nest.Create("spike_generator",
                         params={"spike_times": [10., 15., 55., 70.]})
        pre = nest.Create("parrot_neuron", 5)
        post = nest.Create("parrot_neuron", 5)

        nest.Connect(pre, post, syn_spec="stdp_synapse_rec")
        nest.Connect(sg, pre)

        connections = nest.GetConnections(pre, post)

        weights = np.array([])
        for i in range(100):
            nest.Simulate(1)
            weights = np.append(weights, nest.GetStatus(connections,
                                                        "weight")[0])

        wr_weights = nest.GetStatus(wr, "events")[0]["weights"]

        self.addTypeEqualityFunc(type(wr_weights), self.is_subset)
        self.assertEqual(wr_weights, weights)

    def testMultipleThreads(self):
        """Weight Recorder Multi Threaded"""

        nest.ResetKernel()
        nest.SetKernelStatus({"local_num_threads": 2})

        wr = nest.Create('weight_recorder')
        nest.CopyModel("stdp_synapse", "stdp_synapse_rec",
                       {"weight_recorder": wr[0], "weight": 1.})

        sg = nest.Create("spike_generator",
                         params={"spike_times": [10., 15., 55., 70.]})
        pre = nest.Create("parrot_neuron", 5)
        post = nest.Create("parrot_neuron", 5)

        nest.Connect(pre, post, syn_spec="stdp_synapse_rec")
        nest.Connect(sg, pre)

        connections = nest.GetConnections(pre, post)

        weights = np.array([])
        for i in range(100):
            nest.Simulate(1)
            weights = np.append(weights, nest.GetStatus(connections,
                                                        "weight")[0])

        wr_weights = nest.GetStatus(wr, "events")[0]["weights"]

        self.addTypeEqualityFunc(type(wr_weights), self.is_subset)
        self.assertEqual(wr_weights, weights)

    def testDefinedSenders(self):
        """Weight Recorder Defined Subset Of Senders"""

        nest.ResetKernel()
        nest.SetKernelStatus({"local_num_threads": 1})

        wr = nest.Create('weight_recorder')
        nest.CopyModel("stdp_synapse", "stdp_synapse_rec",
                       {"weight_recorder": wr[0], "weight": 1.})

        sg = nest.Create("spike_generator",
                         params={"spike_times": [10., 15., 55., 70.]})
        pre = nest.Create("parrot_neuron", 5)
        post = nest.Create("parrot_neuron", 5)

        nest.Connect(pre, post, syn_spec="stdp_synapse_rec")
        nest.Connect(sg, pre)

        nest.SetStatus(wr, {"source": pre[:3]})
        connections = nest.GetConnections(pre[:3], post)

        senders = np.array([])
        for i in range(100):
            nest.Simulate(1)
            senders = np.append(senders, nest.GetStatus(connections,
                                                        "source"))

        wr_senders = nest.GetStatus(wr, "events")[0]["senders"]

        self.addTypeEqualityFunc(type(wr_senders), self.is_subset)
        self.assertEqual(wr_senders, senders)

    def testDefinedTargets(self):
        """Weight Recorder Defined Subset Of Targets"""

        nest.ResetKernel()
        nest.SetKernelStatus({"local_num_threads": 1})

        wr = nest.Create('weight_recorder')
        nest.CopyModel("stdp_synapse", "stdp_synapse_rec",
                       {"weight_recorder": wr[0], "weight": 1.})

        sg = nest.Create("spike_generator",
                         params={"spike_times": [10., 15., 55., 70.]})
        pre = nest.Create("parrot_neuron", 5)
        post = nest.Create("parrot_neuron", 5)

        nest.Connect(pre, post, syn_spec="stdp_synapse_rec")
        nest.Connect(sg, pre)

        nest.SetStatus(wr, {"target": post[:3]})
        connections = nest.GetConnections(pre, post[:3])

        targets = np.array([])
        for i in range(100):
            nest.Simulate(1)
            targets = np.append(targets, nest.GetStatus(connections,
                                                        "target"))

        wr_targets = nest.GetStatus(wr, "events")[0]["receivers"]

        self.addTypeEqualityFunc(type(wr_targets), self.is_subset)
        self.assertEqual(wr_targets, targets)


def suite():

    suite = unittest.TestLoader().loadTestsFromTestCase(WeightRecorderTestCase)
    return suite


if __name__ == "__main__":

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
