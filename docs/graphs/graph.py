#!/usr/bin/python

# The purpose of this script is to create a graph that organises and states the
# remainder of my objectives to complete my thesis and final viva. A failure to
# plan is a plan to fail.

from graphviz import Digraph

# A) Define node properties.
shMilestone = {"shape": "octagon", "fontname": "verdana", "style": "filled",
               "fillcolor": "grey15", "fontcolor": "white", "margin": "0,0"}
shTask = {"shape": "egg", "fontname": "verdana", "style": "filled",
          "fillcolor": "white", "margin": "0.1, 0.1"}
shPresent = {"shape": "Msquare", "fontname": "verdana", "style": "filled",
             "fillcolor": "white", "margin": "0.1, 0.1"}
shMiniCluster = {"shape": "square", "fontname": "verdana", "style": "filled"}


# B) Create viva cluster.
vivaClusterName = "Viva"
vivaClusterColour = "lightpink1"
vivaCluster = Digraph(name="cluster_viva", node_attr=shTask)
vivaCluster.body.append("label = \"{}\"".format(vivaClusterName))
vivaCluster.body.append("style = filled")
vivaCluster.body.append("fillcolor = {}".format(vivaClusterColour))

# B) Define viva cluster nodes and edges.
exampleQuestions = "Formulate\nExpected\nQuestions"
reviewThesis = "Review\nThesis"
reviewPapers = "Review\nPapers"
reviewLiterature = "Review\nLiterature"
finalViva = "Final\nViva"
corrections = "Make and\nSubmit\nThesis\nCorrections"
vivaCluster.node(corrections, **shMilestone)
vivaCluster.node(finalViva, **shMilestone)
vivaCluster.edges([(reviewPapers, exampleQuestions),
                   (reviewThesis, exampleQuestions),
                   (reviewLiterature, exampleQuestions),
                   (exampleQuestions, finalViva),
                   (finalViva, corrections)])

# C) Create anisotropy paper cluster.
anisPaperClusterName = "Anisotropy Paper"
anisPaperClusterColour = "aliceblue"
anisPaperCluster = Digraph(name="cluster_anispaper", node_attr=shTask)
anisPaperCluster.body.append("label = \"{}\"".format(anisPaperClusterName))
anisPaperCluster.body.append("style = filled")
anisPaperCluster.body.append("fillcolor = {}".format(anisPaperClusterColour))

# C) Define anisotropy paper cluster nodes and edges.
submitAnisPaper = "Submit\nAnisotropy\nPaper"
postprocess12_21 = "Postprocess\nSimulation\n12_Inv_21\n(increased A & D)"
incorporateAnisPaper = "Incorporate\nResults\nInto Paper"
reviewAnisFeedback = "Review\nFeedback"
designPoster = "Design\nMMM Poster"
createPoster = "Create\nMMM Poster"
presentPoster = "Present\nMMM\nPoster"
reviewPosterFeedback = "Review\n Feedback  "
anisPaperCluster.node(submitAnisPaper, **shMilestone)
anisPaperCluster.node(presentPoster, **shMilestone)
anisPaperCluster.edges([(designPoster, createPoster),
                        (postprocess12_21, createPoster),
                        (createPoster, reviewPosterFeedback),
                        (reviewPosterFeedback, reviewPosterFeedback),
                        (reviewPosterFeedback, presentPoster),
                        (postprocess12_21, incorporateAnisPaper),
                        (reviewAnisFeedback, reviewAnisFeedback),
                        (incorporateAnisPaper, reviewAnisFeedback),
                        (reviewAnisFeedback, reviewPosterFeedback),
                        (reviewPosterFeedback, reviewAnisFeedback),
                        (reviewAnisFeedback, submitAnisPaper)])

# D) Create polycrystalline hysteresis paper cluster.
polyPaperClusterName = "Polycrystalline Paper"
polyPaperClusterColour = "aliceblue"
polyPaperCluster = Digraph(name="cluster_polypaper", node_attr=shTask)
polyPaperCluster.body.append("label = \"{}\"".format(polyPaperClusterName))
polyPaperCluster.body.append("style = filled")
polyPaperCluster.body.append("fillcolor = {}".format(polyPaperClusterColour))

# D) Define polycrystalline hysteresis paper cluster nodes and edges.
submitPolyPaper = "Submit\nPolycrystalline\nHysteresis\nPaper"
draftPolyPaper = "Draft\nPaper"
reviewPolyFeedback = "Review\n Feedback "
communicateCM = "Communicate\nwith Chris\nMarrows"
postprocess15 = "Postprocess\nSimulation 15\n(increased A & D, varying K)"
polyPaperCluster.node(submitPolyPaper, **shMilestone)
polyPaperCluster.edges([(postprocess15, draftPolyPaper),
                        (postprocess15, communicateCM),
                        (communicateCM, postprocess15),
                        (draftPolyPaper, reviewPolyFeedback),
                        (reviewPolyFeedback, communicateCM),
                        (communicateCM, reviewPolyFeedback),
                        (reviewPolyFeedback, reviewPolyFeedback),
                        (reviewPolyFeedback, submitPolyPaper)])

# E) Create virtual micromagnetics paper cluster.
virmagPaperClusterName = "Virtual Micromagnetics Paper"
virmagPaperClusterColour = "aliceblue"
virmagPaperCluster = Digraph(name="cluster_virmag", node_attr=shTask)
virmagPaperCluster.body.append("label = \"{}\"".format(virmagPaperClusterName))
virmagPaperCluster.body.append("style = filled")
virmagPaperCluster.body.append("fillcolor = {}"
                               .format(virmagPaperClusterColour))

# E) Define virtual micromagnetics paper cluster nodes and edges.
submitVirmagPaper = "Submit Virtual\nMicromagnetics\nPaper"
createWebsite = "Create\nHosting\nWebsite"
obtainWWWSpace = "Obtain WWW\nSpace"
hostWebsite = "Host\nWebsite"
reviewVirmagLit = "Review\nLiterature "
draftVirmagPaper = "Draft\nPaper "
idVirmagOutlets = "Identify\nPublication\nOutlets"
testVirtualMachinePerformance = "Test\nVirtual\nMachine\nPerformance"
reviewVirmagFeedback = " Review\nFeedback "
virmagPaperCluster.node(hostWebsite, **shMilestone)
virmagPaperCluster.node(submitVirmagPaper, **shMilestone)
virmagPaperCluster.edges([(idVirmagOutlets, reviewVirmagLit),
                          (reviewVirmagLit, draftVirmagPaper),
                          (testVirtualMachinePerformance, draftVirmagPaper),
                          (createWebsite, obtainWWWSpace),
                          (obtainWWWSpace, hostWebsite),
                          (hostWebsite, submitVirmagPaper),
                          (draftVirmagPaper, reviewVirmagFeedback),
                          (reviewVirmagFeedback, reviewVirmagFeedback),
                          (reviewVirmagFeedback, submitVirmagPaper)])

# F) Define thesis cluster.
thesisClusterName = "Thesis"
thesisClusterColour = "lightpink1"
thesisCluster = Digraph(name="cluster_thesis", node_attr=shTask)
thesisCluster.body.append("label = \"{}\"".format(thesisClusterName))
thesisCluster.body.append("style = filled")
thesisCluster.body.append("fillcolor = {}".format(thesisClusterColour))

# F) Define thesis cluster nodes and edges.
planThesis = "Plan\nThesis"
revisitUpgradeFeedback = "Revisit\nUpgrade\nReview\nFeedback"
resimulateOldResults = "Regenerate\nRelevant\nOld Results"
writeThesis = "Write\nThesis"
submitThesis = "Thesis\nSubmission"
reviewThesisFeedback = "  Review  \nFeedback"
thesisCluster.node(submitThesis, **shMilestone)
thesisCluster.edges([(planThesis, revisitUpgradeFeedback),
                     (revisitUpgradeFeedback, planThesis),
                     (planThesis, resimulateOldResults),
                     (resimulateOldResults, writeThesis),
                     (writeThesis, reviewThesisFeedback),
                     (reviewThesisFeedback, reviewThesisFeedback),
                     (reviewThesisFeedback, submitThesis)])

# G) Define literature review cluster.
literatureClusterName = "Literature Review"
literatureClusterColour = "palegreen1"
literatureCluster = Digraph(name="cluster_literature", node_attr=shTask)
literatureCluster.body.append("label = \"{}\"".format(literatureClusterName))
literatureCluster.body.append("style = filled")
literatureCluster.body.append("fillcolor = {}".format(literatureClusterColour))

# G) Define literature review cluster nodes and edges.
extensiveLiteratureReview = "Re-review\nLiterature\nExtensively"
createTimeline = "Create\nLiterature\nTimeline"
startPaperReviewGroup = "Start\nPaper\nReview\nGroup"
literatureCluster.node(startPaperReviewGroup, **shMilestone)
literatureCluster.edges([(startPaperReviewGroup, extensiveLiteratureReview),
                         (extensiveLiteratureReview, createTimeline),
                         (createTimeline, extensiveLiteratureReview)])

# V) Create master graph and connect subgraphs.
masterGraph = Digraph(name="post_upgrade_digraph_full", node_attr=shPresent,
                      graph_attr={"rankdir": "UD", "page": "8.5,11"})
masterGraph.subgraph(vivaCluster)
masterGraph.subgraph(anisPaperCluster)
masterGraph.subgraph(polyPaperCluster)
masterGraph.subgraph(virmagPaperCluster)
masterGraph.subgraph(thesisCluster)
masterGraph.subgraph(literatureCluster)

# W) Define master graph nodes and edges.
postUpgrade = "Post\nUpgrade\nViva"
holiday = "Holiday"
masterGraph.edges([(postUpgrade, postprocess12_21),
                   (postUpgrade, designPoster),
                   (postUpgrade, postprocess15),
                   (postUpgrade, idVirmagOutlets),
                   (postUpgrade, testVirtualMachinePerformance),
                   (postUpgrade, extensiveLiteratureReview),
                   (postUpgrade, createWebsite),
                   (postUpgrade, planThesis),
                   (postUpgrade, startPaperReviewGroup),
                   (submitAnisPaper, writeThesis),
                   (submitAnisPaper, reviewPapers),
                   (submitPolyPaper, writeThesis),
                   (submitPolyPaper, reviewPapers),
                   (submitVirmagPaper, writeThesis),
                   (submitVirmagPaper, reviewPapers),
                   (extensiveLiteratureReview, writeThesis),
                   (submitThesis, reviewThesis),
                   (submitThesis, reviewLiterature),
                   (corrections, holiday)])

# X) Create reduced graph.
miniGraph = Digraph(name="post_upgrade_digraph_reduced",
                    graph_attr={"rankdir": "UD"})
miniGraph.node(postUpgrade, **shPresent)
miniGraph.node(holiday, **shPresent)
miniGraph.node(vivaClusterName, fillcolor=vivaClusterColour, **shMiniCluster)
miniGraph.node(thesisClusterName, fillcolor=vivaClusterColour, **shMiniCluster)
miniGraph.node(anisPaperClusterName, fillcolor=anisPaperClusterColour,
               **shMiniCluster)
miniGraph.node(virmagPaperClusterName, fillcolor=virmagPaperClusterColour,
               **shMiniCluster)
miniGraph.node(polyPaperClusterName, fillcolor=polyPaperClusterColour,
               **shMiniCluster)
miniGraph.node(literatureClusterName, fillcolor=literatureClusterColour,
               **shMiniCluster)

miniGraph.edges([(postUpgrade, thesisClusterName),
                 (postUpgrade, anisPaperClusterName),
                 (postUpgrade, virmagPaperClusterName),
                 (postUpgrade, polyPaperClusterName),
                 (postUpgrade, literatureClusterName),
                 (anisPaperClusterName, thesisClusterName),
                 (anisPaperClusterName, vivaClusterName),
                 (virmagPaperClusterName, thesisClusterName),
                 (virmagPaperClusterName, vivaClusterName),
                 (polyPaperClusterName, thesisClusterName),
                 (polyPaperClusterName, vivaClusterName),
                 (literatureClusterName, thesisClusterName),
                 (thesisClusterName, vivaClusterName),
                 (vivaClusterName, holiday)])

# Z) Print graphs.
masterGraph.render(cleanup=True)
miniGraph.render(cleanup=True)
