#include <fcntl.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <unistd.h>
#include <dirent.h>
#include <strings.h>
#include <pwd.h>

#define BUFFER_SIZE 100
char buf[100];

void pisz_sciezke(){
    static int first_time=1;
    if(first_time){
        const char* CLEAR_SCRENN_ANSI="\e[1;1H\e[2J";
        write(STDOUT_FILENO,CLEAR_SCRENN_ANSI,12);
        printf("    \n ZNAJDUJESZ SIE W POWLOCE MICROSHELL \n\n");
        printf("  ABY ZAKONCZYC DZIALANIE POWLOKI WPISZ: exit\n");
        printf("  ABY WYSWIETLIC WIECEJ INFORMACJI WPISZ: help\n\n"); 
        first_time=0;
    }
    char *name,*path; 
    struct passwd *pass; 
    pass=getpwuid(getuid()); 
    name=pass->pw_name;         //nazwa uzytkownika

    if( (path=getcwd(NULL, 0)) == NULL) {
        perror("nie udalo sie pobrac sciezki path\n");}
    else printf("%c[%dm[%s:%c[%dm%s%c[%dm]\n$ ",0x1B,1,name,0x1B,33,path,0x1B,0);
    //kolorki %c[%dm [
}

void help(){
    printf("    \n        MICROSHELL          \n");
    printf("     autor ZUZANNA GOLEBIEWSKA   \n");
    printf("    Informatyka rok ,I grupa 12 \n\n");
    printf("Oto dostepne dla ciebie komendy:\n--help\n--cd(~,..)\n--ls(-a)\n--pwd\n--type\n\n");
}

void ls(const char *sciezka) {
    struct dirent *plik;
    DIR *sciezka1;
    if((sciezka1=opendir(sciezka))) {
        while((plik=readdir(sciezka1)))
             puts(plik->d_name);
        closedir(sciezka1);
    }
    else perror("Nie udalo sie pobrac strumienia sciezki\n"); 
}

int prefix(char const *p, char const *q){
    int i = 0;
    for(i = 0;q[i];i++)
        if(p[i] != q[i])
            return -1;
    return 0;
}

/*void cd(char *pth){
    char sciezka[BUFFER_SIZE],cwd[BUFFER_SIZE];
    strcpy(sciezka,pth);

    if(pth[0]!= '/'){
        getcwd(cwd,sizeof(cwd));
        strcat(cwd,"/");
        strcat(cwd,sciezka);
        chdir(cwd);
    }else chdir(pth);
}*/

int cd(char **args)
{
  if (args[1] == NULL) {
    fprintf(stderr, "lsh: expected argument to \"cd\"\n");
  } else {
    if (chdir(args[1]) != 0) {
      perror("lsh");
    }
  }
  return 1;
}


void pwd(){
    char *path;
    if( (path=getcwd(NULL, 0)) == NULL) {
        perror("nie udalo sie pobrac sciezki path\n");}
    else printf("%s\n",path);
}

  
int main(void)
{
        char *tok,wejscie[BUFFER_SIZE];
        //char *envp[]={(char *)"PATH=/bin",0};       

         while(1){
            pisz_sciezke();
            fgets(wejscie,50,stdin);

            if(strcmp(wejscie,"exit\n")==0)
                return 0;
            else if(prefix(wejscie,"cd")==0){
                tok=strchr(wejscie,' ');
                printf("tok = %s\t",tok);
                if(tok){
                    char *temptok=tok+1;
                    tok=temptok;
                    char *nline=strchr(tok,'\n');
                    printf("tok= %s nline = %s\t",tok,nline);
                    if(nline)
                        nline='\0';
                    cd(tok);    
                } else printf("blad\n"); 
            }
            else if(strcmp(wejscie,"help\n")==0)
                help(); 
            else if(strcmp(wejscie,"ls\n")==0)
                ls(".");
            else if(prefix(wejscie,"echo")==0){
                     tok=strchr(wejscie,' ');
                    printf("%s",tok);

                }
            else if(prefix(wejscie,"type")==0){
                    tok=strchr(wejscie,' ');
                    if(tok){
                        if(strcmp(tok," help\n")==0)
                            printf("help wyswietla pomocnicze informacje\n");
                        else if(strcmp(tok," ls\n")==0)
                            printf("ls listuje zawartosc katalogu w ktorym obecnie sie znajdujesz\n");
                        else if(strcmp(tok," cd\n")==0)
                            printf("cd przenosi cie do innego katalogu\n");
                        else if(strcmp(tok," echo\n")==0)
                            printf("echo wyswietla tok na standardowe wyjscie\n");
                        else if(strcmp(tok," pwd\n")==0)
                            printf("pwd zwraca aktualna sciezke do katalogu roboczego\n");
                        else perror("nie rozpoznano polecenia\n");
                    }else perror("nie rozpoznano polecenia\n");
            }else perror("Nie rozpoznano komendy\n");
            
         }
    

    exit(EXIT_SUCCESS);
}