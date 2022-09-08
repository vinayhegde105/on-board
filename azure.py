import os
from getpass import getpass

print("---------------------------------------------------------------------------------------------------------")
folder = int(input("Kindly Select your task:\n1.Azure IaC Project       2.centralized logging setup      3.Add service connection to ADO Project       \n\nYour input: "))

if folder == 1:
    print("---------------------------------------------------------------------------------------------------------")
    ado_agent = int(input("Kindly select your agent type to provision ADO...\n1.Cloud-hosted pool       2.Selfhosted AKS pool       3.Selfhosted VMSS pool      4.ADD selfhosted agent to ADO\n\nYour input:"))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")

    if ado_agent == 1:
        print("---------------------------------------------------------------------------------------------------------")
        script_choice = int(input("Select your Task:\n1.Create       2.Update       3.Destroy\nYour input: "))
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/azure_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/azure_onboard")
        os.system("git sparse-checkout add ado_construction/cloudhosted")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/azure_onboard/ado_construction/cloudhosted")
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
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/azure_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/azure_onboard")
        os.system("git sparse-checkout add ado_construction/selfhosted_aks")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/azure_onboard/ado_construction/selfhosted_aks")
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
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/azure_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/azure_onboard")
        os.system("git sparse-checkout add ado_construction/selfhosted_vmss")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/azure_onboard/ado_construction/selfhosted_vmss")
        if script_choice==1:
            exec(open("create.py").read())
        elif script_choice ==2:
            exec(open("update.py").read())
        elif script_choice ==3:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    # elif ado_agent == 4:
    #     os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/azure_onboard")
    #     cwd = os.getcwd()
    #     os.chdir(f"{cwd}/azure_onboard")
    #     os.system("git sparse-checkout add 1.ado_construction/add_ec2_agent")
    #     if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    #     os.chdir(f"{cwd}/azure_onboard/1.ado_construction/add_ec2_agent")
    #     exec(open("add.py").read())
    else:
        print("Wrong input received...")

elif folder==2:
    print("---------------------------------------------------------------------------------------------------------")
    # script_choice = int(input("Select your Task:\n1.Create       2.Destroy"))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/azure_onboard")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/azure_onboard")
    os.system("git sparse-checkout add centralized_logging")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    os.chdir(f"{cwd}/azure_onboard/centralized_logging")
    exec(open("create.py").read())
    # if script_choice==1:
    #     exec(open("create.py").read())
    # elif script_choice ==2:
    #     exec(open("destroy.py").read())
    # else:
    #     print("Wrong input received...")

elif folder==3:
    print("---------------------------------------------------------------------------------------------------------")
    script_choice = int(input("How many Service Connection you want to add:\n1.ONE       2.TWO       3.THREE\nYour input: "))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/azure_onboard")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/azure_onboard")
    os.system("git sparse-checkout add serviceconnection")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if script_choice==1:
        sc_choice = int(input("Select your Task:\n1.Create     2.Destroy"))
        os.chdir(f"{cwd}/azure_onboard/serviceconnection/add_one_service_connection_ado")
        if sc_choice == 1:
            exec(open("create.py").read())
        elif sc_choice ==2:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    elif script_choice ==2:
        sc_choice = int(input("Select your Task:\n1.Create     2.Destroy"))
        os.chdir(f"{cwd}/azure_onboard/serviceconnection/add_two_service_connection_ado")
        if sc_choice == 1:
            exec(open("create.py").read())
        elif sc_choice ==2:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    elif script_choice ==3:
        sc_choice = int(input("Select your Task:\n1.Create     2.Destroy"))
        os.chdir(f"{cwd}/azure_onboard/serviceconnection/add_three_service_connection_ado")
        if sc_choice == 1:
            exec(open("create.py").read())
        elif sc_choice ==2:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    else:
        print("Wrong input received...")

else:
    print("Wrong input received...")

