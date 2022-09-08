import os
from getpass import getpass

print("---------------------------------------------------------------------------------------------------------")
folder = int(input("Kindly Select your task:\n1.GCP IaC Project         2.Centralized logging setup        3.Add service connection to ADO Project \n\nYour input: "))

if folder == 1:
    print("---------------------------------------------------------------------------------------------------------")
    ado_agent = int(input("Kindly select your agent type to provision ADO...\n1.cloud-hosted pool       2.Selfhosted GKE pool       3.Selfhosted Intance Group pool      4.ADD selfhosted agent to ADO\n\nYour input:"))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")

    if ado_agent == 1:
        print("---------------------------------------------------------------------------------------------------------")
        script_choice = int(input("Select your Task:\n1.Create       2.Update       3.Destroy\nYour input: "))
        # os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Development-Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/gcp_onboard")
        os.system("git sparse-checkout add ado_construction/cloudhosted")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/gcp_onboard/ado_construction/cloudhosted")
        if script_choice==1:
            exec(open("create.py").read())
        elif script_choice ==2:
            exec(open("update.py").read())
        elif script_choice ==3:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    elif ado_agent == 2:
        print("---------------------------------------------------------------------------------------------------------")
        script_choice = int(input("Select your Task:\n1.Create       2.Update       3.Destroy\nYour input: "))
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/gcp_onboard")
        os.system("git sparse-checkout add ado_construction/selfhosted_gke")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/gcp_onboard/ado_construction/selfhosted_gke")
        if script_choice==1:
            exec(open("create.py").read())
        elif script_choice ==2:
            exec(open("update.py").read())
        elif script_choice ==3:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    elif ado_agent == 3:
        print("---------------------------------------------------------------------------------------------------------")
        script_choice = int(input("Select your Task:\n1.Create       2.Update       3.Destroy\nYour input: "))
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/gcp_onboard")
        os.system("git sparse-checkout add ado_construction/instance_group")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/gcp_onboard/ado_construction/instance_group")
        if script_choice==1:
            exec(open("create.py").read())
        elif script_choice ==2:
            exec(open("update.py").read())
        elif script_choice ==3:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    elif ado_agent == 4:
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/gcp_onboard")
        os.system("git sparse-checkout add ado_construction/add_singleVM_pool")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/gcp_onboard/ado_construction/add_singleVM_pool")
        exec(open("create.py").read())
    else:
        print("Wrong input received...")

# elif folder==2:
#     print("---------------------------------------------------------------------------------------------------------")
#     script_choice = int(input("Select your Task:\n1.Create       2.Destroy"))
#     print("---------------------------------------------------------------------------------------------------------")
#     centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
#     os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
#     cwd = os.getcwd()
#     os.chdir(f"{cwd}/gcp_onboard")
#     os.system("git sparse-checkout add 2.AFT_setup")
#     if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
#     os.chdir(f"{cwd}/gcp_onboard/2.AFT_setup")
#     if script_choice==1:
#         exec(open("create_AFT.py").read())
#     elif script_choice ==2:
#         exec(open("destroy_AFT.py").read())
#     else:
#         print("Wrong input received...")

elif folder==3:
    print("---------------------------------------------------------------------------------------------------------")
    script_choice = int(input("How many Service Connection you want to add:\n1.ONE       2.TWO       3.THREE\nYour input: "))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/gcp_onboard")
    os.system("git sparse-checkout add service_connection")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if script_choice==1:
        os.chdir(f"{cwd}/gcp_onboard/service_connection/add_one_sc")
        exec(open("create.py").read())
    elif script_choice ==2:
        os.chdir(f"{cwd}/gcp_onboard/service_connection/add_two_sc")
        exec(open("create.py").read())
    elif script_choice ==3:
        os.chdir(f"{cwd}/gcp_onboard/service_connection/add_three_sc")
        exec(open("create.py").read())
    else:
        print("Wrong input received...")

# elif folder==4:
#     print("---------------------------------------------------------------------------------------------------------")
#     script_choice = int(input("Select your Task:\n1.Setup Logging       2.add accounts to exsisting logging       3.Destroy logging\nYour input: "))
#     centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
#     os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/gcp_onboard")
#     print("---------------------------------------------------------------------------------------------------------")
#     cwd = os.getcwd()
#     os.chdir(f"{cwd}/gcp_onboard")
#     os.system("git sparse-checkout add 4.centralized_logging")
#     if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
#     if script_choice==1:
#         os.chdir(f"{cwd}/gcp_onboard/4.centralized_logging/working_directory")
#         exec(open("create.py").read())
#     elif script_choice ==2:
#         os.chdir(f"{cwd}/gcp_onboard/4.centralized_logging/working_directory/add_accounts")
#         exec(open("add_accounts.py").read())
#     elif script_choice ==3:
#         os.chdir(f"{cwd}/gcp_onboard/4.centralized_logging/working_directory/destroy_logging")
#         exec(open("destroy.py").read())
#     else:
#         print("Wrong input received...")
    
else:
    print("Wrong input received...")

