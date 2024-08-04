#ifndef ROMIROBOT_H
#define ROMIROBOT_H

#ifdef __cplusplus
#pragma once
extern "C" {
#endif

const char* romirobot_git_version(void);
const char* romirobot_git_revision(void);
const char* romirobot_git_branch(void);

/** @brief A very interesting function!
 *
 * This function is of course just a self-explanatory placeholder,
 * but surprisingly often, things aren't this easy. You should
 * therefore *really* document your C++ code with Doxygen!
 *
 * @param x The number to increase
 * @returns the successor of x
 */
int add_one(int x);

#ifdef __cplusplus
}
#endif

#endif  // ROMIROBOT_H
