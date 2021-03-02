struct API
{
   int(*read) (char *raft_uuid, char *peer_uuid);
   int(*write) (char *raft_uuid, char *peer_uuid);
};

void call_python_func(struct API *my_api);