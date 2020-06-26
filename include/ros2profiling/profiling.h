#ifndef ROS2PROFILING_H
#define ROS2PROFILING_H

#ifdef __cplusplus
extern "C" {
#endif

#include <time.h>
#include <string.h>

/* #define PROFIDX_RMW_TAKE_WITH_INFO 0 */
/* #define PROFIDX_RCL_TAKE 1 */
/* #define PROFIDX_TAKE_TYPE_ERASED 2 */
/* #define PROFIDX_RMW_PUBLISH 3 */
/* #define PROFIDX_RCL_PUBLISH 4 */
/* #define PROFIDX_HANDLE_MSG 5 */
/* #define PROFIDX_DO_INTER_PROCESS_PUBLISH 6 */
  
#define PROFIDX_PUB_RCLCPP_INTERPROCESS_PUBLISH 1
#define PROFIDX_PUB_RCL_PUBLISH 2
#define PROFIDX_PUB_RMW_PUBLISH 3
#define PROFIDX_PUB_DDS_WRITE 4  


#define PROFIDX_SUB_DDS_ONDATA 8
#define PROFIDX_SUB_RCLCPP_TAKE 9
#define PROFIDX_SUB_RCL_TAKE 10
#define PROFIDX_SUB_RMW_TAKE_WITH_INFO 11
#define PROFIDX_SUB_DDS_TAKE 12
  
#define PROFIDX_SUB_RCLCPP_HANDLE 18

  static uint64_t get_timestamp() {
    long int ns;
    uint64_t all;
    time_t sec;
    struct timespec spec;

    clock_gettime(CLOCK_REALTIME, &spec);
    sec = spec.tv_sec;
    ns = spec.tv_nsec;

    all = (uint64_t) sec * 1000000000UL + (uint64_t) ns;
    
  }
  
  static void store_profile(const char* topic_name, void* msg, int profile_index, const char* log_msg, uint64_t* ts) {

    if (strstr(topic_name, "_profile_") == NULL)
      return;

    uint64_t ts_val;
    if (ts)
      ts_val = *ts;
    else
      ts_val = get_timestamp();

    uint64_t* msg_u64 = (uint64_t*)msg;
    const int data_offset = 6;
    msg_u64[profile_index + data_offset] = ts_val;

    #ifdef _DEBUG
    if (log_msg)
      printf("%lu %s %s\n", ts_val, topic_name, log_msg);
    else {
      printf("%lu %s\n", ts_val, topic_name);
    }
    #endif
  }

  static uint64_t get_profile(const void* msg, int profile_index) {
    const uint64_t* msg_u64 = (const uint64_t*)msg;
    const int data_offset = 6;
    return msg_u64[profile_index + data_offset];
  }

#ifdef __cplusplus
}
#endif


#endif

