typedef struct PmdbAPI PmdbAPI;
struct PmdbAPI
{
  int a;
  float b;
};
void show_somedata(PmdbAPI somedata);
void struct_by_ref(PmdbAPI *somedata);
PmdbAPI get_somedata(int a, float b);
void library_function(int (*fun_ptr)(int, int), int x, int y);