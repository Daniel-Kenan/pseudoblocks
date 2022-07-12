#include <stdio.h>
#include <string.h>
#include <windows.h>
int main () {
   char command[50];
   SetConsoleTitle("PseudoBlocks v1.0.03 (64-bit)");
   strcpy( command, "cmd /k setup.cmd" );
   system(command);

   return(0);
}
