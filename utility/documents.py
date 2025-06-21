# print("documents loading...")

from utility.config import client
import pandas as pd # documents reading 

# file paths
# add path 
path = "utility/content/"
bns=path+'sections_db.csv'
# articles=path+'constitution_articles.csv'
bnss=path+'bnss.csv'
evidence=path+'evidence_law.csv'
vehicle = path+'motor_vehicle_law.csv'
womenprotect = path+'women_protection.csv'
humanrights = path+'human_rights.csv'
#--- file paths end


# --- load dataset
df_bns = pd.read_csv(bns)
# df_articles = pd.read_csv(articles)
df_bnss = pd.read_csv(bnss)
df_evidence = pd.read_csv(evidence)
df_vehicle = pd.read_csv(vehicle)
df_womenprotect = pd.read_csv(womenprotect)
df_humanrights = pd.read_csv(humanrights)
# --- load dataset end


# loading -- bnss
def BNS():
    sample_bns = client.files.upload(
        file=bns,
        config=dict(mime_type='text/csv'),
    )
    return sample_bns

# # loading -- ipc  (*Postepone till next update*)
# def IPC():
#     sample_articles = client.files.upload(
#         file=articles,
#         config=dict(mime_type='text/csv'),
#     )
#     return sample_articles

# loading -- bnss
def BNSS():
    sample_bnss = client.files.upload(
        file=bnss,
        config=dict(mime_type='text/csv'),
    )
    return sample_bnss

# loading -- evidence law
def EVIDENCE():
    sample_evidence = client.files.upload(
        file=evidence,
        config=dict(mime_type='text/csv'),
    )
    return sample_evidence

# loading -- vehicle
def VEHICLE():
    sample_mvehicle = client.files.upload(
        file=vehicle,
        config=dict(mime_type='text/csv'),
    )
    return sample_mvehicle

# loading -- woman protection
def WOMEN_PROTECTION():
    sample_womenprotect = client.files.upload(
        file=womenprotect,
        config=dict(mime_type='text/csv'),
    )
    return sample_womenprotect

# loading -- human rights
def HUMAN_RIGHTS():
    sample_humanrights = client.files.upload(
        file=humanrights,
        config=dict(mime_type='text/csv'),
    )
    return sample_humanrights


# print("BNS ",BNS())
# print("BNSS ",BNSS())
# print("IPC ",IPC())
# print("EVIDEMCE ",EVIDENCE())
# print("vehicle ",VEHICLE())
# print("women protection ",WOMEN_PROTECTION())
# print("Human rights ",HUMAN_RIGHTS())
# print("documents end loading...")
