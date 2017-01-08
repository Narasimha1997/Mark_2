#include<stdio.h>
#include<stdlib.h>

FILE *installer;
void run(){
    int exit_status, exit_status2;
    exit_status=system("python --versiob");
    if(exit_status==1){
        printf("Error launching the application, Download python interpreter 3.0 or above and configure it properly");
    }
    else{
        exit_status2=system("python interface.py");
        printf("Done...");
    }
}

void install_configure(int condn){
    installer=fopen("installer_data.txt","w");
    if (condn==1)
        fprintf(installer,"%d", 0);
    if(condn==2)
        fprintf(installer,"%d", 1);
    if(condn==3)
        fprintf(installer,"%d", 2);
    fclose(installer);
    system("python install.py");
}

void main(){
    int ch, inst_choice;
    for(;;){
        printf("1. Run application \n2. Install (Repair) or configure\n3.Exit\n");
        scanf("%d", &ch);
        switch (ch)
        {
            case 1: run();break;
            case 2: 
               printf("\n---------------CONTROL PANEL-------------------\n");
               printf("1. Full install[Requires internet]\n2. Confgure only\n3. Install dependencies [Requires internet]\n");
               scanf("%d", &inst_choice);
               switch(inst_choice){
                   case 1: install_configure(1); break;
                   case 2: install_configure(2); break;
                   case 3: install_configure(3); break;
                   default: break;
               }
               break;
               case 3: exit(0);
        }
    }
}