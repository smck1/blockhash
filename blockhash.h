#if _WINDOWS
	#define declspec __declspec(dllexport)
#else
	#define declspec
#endif

declspec char* blockhash_quick_string(int bits, unsigned char *data, int width, int height);

declspec char* blockhash_string(int bits, unsigned char *data, int width, int height);

declspec void release_hash_string(char* hash);