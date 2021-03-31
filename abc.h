struct pmdb_callback_ptr {
	int (*applycb_ptr)(char *raft_uuid, char *peer_uuid);
	int (*readcb_ptr)(char *raft_uuid, char *peer_uuid);
};

void example(int (*fun_ptr)(int, int), int x, int y, void* data);
