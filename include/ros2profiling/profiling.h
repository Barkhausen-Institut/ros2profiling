#ifndef ROS2PROFILING_H
#define ROS2PROFILING_H

#ifdef __cplusplus
extern "C" {
#endif

#include <time.h>
#include <string.h>

#define PROFIDX_RMW_TAKE_WITH_INFO 0
#define PROFIDX_RCL_TAKE 1
#define PROFIDX_TAKE_TYPE_ERASED 2
#define PROFIDX_RMW_PUBLISH 3
#define PROFIDX_RCL_PUBLISH 4
#define PROFIDX_HANDLE_MSG 5
#define PROFIDX_DO_INTER_PROCESS_PUBLISH 6

static void store_profile(const char* topic_name, void* msg, int profile_index, const char* log_msg) {

  if (strstr(topic_name, "_profile_") == NULL)
    return;

  long int ns;
  uint64_t all;
  time_t sec;
  struct timespec spec;

  clock_gettime(CLOCK_REALTIME, &spec);
  sec = spec.tv_sec;
  ns = spec.tv_nsec;

  all = (uint64_t) sec * 1000000000UL + (uint64_t) ns;

  uint64_t* msg_u64 = (uint64_t*)msg;
  const int data_offset = 4;
  msg_u64[profile_index + data_offset] = all;

  if (log_msg)
    printf("%lu %s %s\n", all, topic_name, log_msg);
  else {
    printf("%lu %s\n", all, topic_name);
  }
}

  static uint64_t get_profile(void* msg, int profile_index) {
    uint64_t* msg_u64 = (uint64_t*)msg;
    const int data_offset = 4;
    return msg_u64[profile_index + data_offset];
  }

#ifdef __cplusplus
}
#endif


#endif

