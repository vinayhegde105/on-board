import os
from getpass import getpass

print("---------------------------------------------------------------------------------------------------------")
folder = int(input("Kindly Select your task:\n1.AWS IaC Project         2.AFT Setup        3.Add service connection to ADO Project       4.centralized logging setup\n\nYour input: "))

if folder == 1:
    print("---------------------------------------------------------------------------------------------------------")
    ado_agent = int(input("Kindly select your agent type to provision ADO...\n1.cloud-hosted pool       2.Selfhosted EKS pool       3.Selfhosted ASG pool      4.ADD selfhosted agent to ADO\n\nYour input:"))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")

    if ado_agent == 1:
        print("---------------------------------------------------------------------------------------------------------")
        script_choice = int(input("Select your Task:\n1.Create       2.Update       3.Destroy\nYour input: "))
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/aws_onboard")
        os.system("git sparse-checkout add 1.ado_construction/cloudhosted")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/aws_onboard/1.ado_construction/cloudhosted")
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
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/aws_onboard")
        os.system("git sparse-checkout add 1.ado_construction/selfhosted_eks")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/aws_onboard/1.ado_construction/selfhosted_eks")
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
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/aws_onboard")
        os.system("git sparse-checkout add 1.ado_construction/selfhosted_asg")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/aws_onboard/1.ado_construction/selfhosted_asg")
        if script_choice==1:
            exec(open("create.py").read())
        elif script_choice ==2:
            exec(open("update.py").read())
        elif script_choice ==3:
            exec(open("destroy.py").read())
        else:
            print("Wrong input received...")
    elif ado_agent == 4:
        os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
        cwd = os.getcwd()
        os.chdir(f"{cwd}/aws_onboard")
        os.system("git sparse-checkout add 1.ado_construction/add_ec2_agent")
        if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
        os.chdir(f"{cwd}/aws_onboard/1.ado_construction/add_ec2_agent")
        exec(open("add.py").read())
    else:
        print("Wrong input received...")

elif folder==2:
    print("---------------------------------------------------------------------------------------------------------")
    script_choice = int(input("Select your Task:\n1.Create       2.Destroy"))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/aws_onboard")
    os.system("git sparse-checkout add 2.AFT_setup")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    os.chdir(f"{cwd}/aws_onboard/2.AFT_setup")
    if script_choice==1:
        exec(open("create_AFT.py").read())
    elif script_choice ==2:
        exec(open("destroy_AFT.py").read())
    else:
        print("Wrong input received...")

elif folder==3:
    print("---------------------------------------------------------------------------------------------------------")
    script_choice = int(input("How many Service Connection you want to add:\n1.ONE       2.TWO       3.THREE\nYour input: "))
    print("---------------------------------------------------------------------------------------------------------")
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/aws_onboard")
    os.system("git sparse-checkout add 3.service_connection")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if script_choice==1:
        os.chdir(f"{cwd}/aws_onboard/3.service_connection/one_sc_add")
        exec(open("create.py").read())
    elif script_choice ==2:
        os.chdir(f"{cwd}/aws_onboard/3.service_connection/two_sc_add")
        exec(open("create.py").read())
    elif script_choice ==3:
        os.chdir(f"{cwd}/aws_onboard/3.service_connection/three_sc_add")
        exec(open("create.py").read())
    else:
        print("Wrong input received...")

elif folder==4:
    print("---------------------------------------------------------------------------------------------------------")
    script_choice = int(input("Select your Task:\n1.Setup Logging       2.add accounts to exsisting logging       3.Destroy logging\nYour input: "))
    centralizedpat = getpass("Enter Insight Central repo PAT tocken: ")
    os.system(f"git clone --sparse --filter=blob:none --depth=1 https://{centralizedpat}@dev.azure.com/nsitmspdevops/Insight%20CMP%20Centralized%20Repository/_git/aws_onboard")
    print("---------------------------------------------------------------------------------------------------------")
    cwd = os.getcwd()
    os.chdir(f"{cwd}/aws_onboard")
    os.system("git sparse-checkout add 4.centralized_logging")
    if os.path.exists("azure-pipelines.yml"): os.system("rm azure-pipelines.yml")
    if script_choice==1:
        os.chdir(f"{cwd}/aws_onboard/4.centralized_logging/working_directory")
        exec(open("create.py").read())
    elif script_choice ==2:
        os.chdir(f"{cwd}/aws_onboard/4.centralized_logging/working_directory/add_accounts")
        exec(open("add_accounts.py").read())
    elif script_choice ==3:
        os.chdir(f"{cwd}/aws_onboard/4.centralized_logging/working_directory/destroy_logging")
        exec(open("destroy.py").read())
    else:
        print("Wrong input received...")
    
else:
    print("Wrong input received...")

