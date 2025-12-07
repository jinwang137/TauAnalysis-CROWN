from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup, Filter

####################
# Set of producers used for get pt, eta, phi, mass from p4
####################

tt_fatjet_pt = Producer(
    name="tt_fatjet_pt",
    call='quantities::boostedbbtt::pt({df}, {output}, {input})',
    input=[
      q.fatjet_p4_0,
    ],
    output=[q.fatjet_pt_tt],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
tt_fatjet_eta = Producer(
    name="tt_fatjet_eta",
    call='quantities::boostedbbtt::eta({df}, {output}, {input})',
    input=[
      q.fatjet_p4_0,
    ],
    output=[q.fatjet_eta_tt],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
tt_fatjet_phi = Producer(
    name="tt_fatjet_phi",
    call='quantities::boostedbbtt::phi({df}, {output}, {input})',
    input=[
      q.fatjet_p4_0,
    ],
    output=[q.fatjet_phi_tt],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
tt_fatjet_mass = Producer(
    name="tt_fatjet_mass",
    call='quantities::boostedbbtt::mass({df}, {output}, {input})',
    input=[
      q.fatjet_p4_0,
    ],
    output=[q.fatjet_mass_tt],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)

bb_fatjet_pt = Producer(
    name="bb_fatjet_pt",
    call='quantities::boostedbbtt::pt({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_pt_bb],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
bb_fatjet_eta = Producer(
    name="bb_fatjet_eta",
    call='quantities::boostedbbtt::eta({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_eta_bb],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
bb_fatjet_phi = Producer(
    name="bb_fatjet_phi",
    call='quantities::boostedbbtt::phi({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_phi_bb],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
bb_fatjet_mass = Producer(
    name="bb_fatjet_mass",
    call='quantities::boostedbbtt::mass({df}, {output}, {input})',
    input=[
      q.fatjet_p4_1,
    ],
    output=[q.fatjet_mass_bb],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)

BoostedTau_0_pt = Producer(
    name="BoostedTau_0_pt",
    call='quantities::boostedbbtt::pt({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_0,
    ],
    output=[q.tau_pt_0],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
BoostedTau_0_eta = Producer(
    name="BoostedTau_0_eta",
    call='quantities::boostedbbtt::eta({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_0,
    ],
    output=[q.tau_eta_0],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
BoostedTau_0_phi = Producer(
    name="BoostedTau_0_phi",
    call='quantities::boostedbbtt::phi({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_0,
    ],
    output=[q.tau_phi_0],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
BoostedTau_0_mass = Producer(
    name="BoostedTau_0_mass",
    call='quantities::boostedbbtt::mass({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_0,
    ],
    output=[q.tau_mass_0],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)

BoostedTau_1_pt = Producer(
    name="BoostedTau_1_pt",
    call='quantities::boostedbbtt::pt({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_1,
    ],
    output=[q.tau_pt_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
BoostedTau_1_eta = Producer(
    name="BoostedTau_1_eta",
    call='quantities::boostedbbtt::eta({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_1,
    ],
    output=[q.tau_eta_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
BoostedTau_1_phi = Producer(
    name="BoostedTau_1_phi",
    call='quantities::boostedbbtt::phi({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_1,
    ],
    output=[q.tau_phi_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
BoostedTau_1_mass = Producer(
    name="BoostedTau_1_mass",
    call='quantities::boostedbbtt::mass({df}, {output}, {input})',
    input=[
      q.BoostedTau0_p4_1,
    ],
    output=[q.tau_mass_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)


HH_pt = Producer(
    name="HH_pt",
    call='quantities::boostedbbtt::pt({df}, {output}, {input})',
    input=[
      q.HH_p4,
    ],
    output=[q.HH_pt_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
HH_eta = Producer(
    name="HH_eta",
    call='quantities::boostedbbtt::eta({df}, {output}, {input})',
    input=[
      q.HH_p4,
    ],
    output=[q.HH_eta_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
HH_phi = Producer(
    name="HH_phi",
    call='quantities::boostedbbtt::phi({df}, {output}, {input})',
    input=[
      q.HH_p4,
    ],
    output=[q.HH_phi_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
HH_mass = Producer(
    name="HH_mass",
    call='quantities::boostedbbtt::mass({df}, {output}, {input})',
    input=[
      q.HH_p4,
    ],
    output=[q.HH_mass_1],
    scopes=["boostedbb_boostedtt",  "boostedbb_boostedtt_subjet", "boostedbb_boostedtt_fatjet"],
)
