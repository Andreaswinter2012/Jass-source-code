#include <stdlib.h>
#include <unistd.h>
int main(int argc, char *argv[]) {
  char path[1024];
  snprintf(path, sizeof(path), "%s/usr/src/launcher.sh", getenv("APPDIR"));
  argv[0] = path;
  execv(path, argv);
  return 1;
}
