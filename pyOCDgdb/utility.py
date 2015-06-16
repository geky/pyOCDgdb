"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2015 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

## @brief Convert string of hex bytes to list of integers.
def hexStringToIntList(data):
    i = 0
    result = []
    while i < len(data):
        result.append(int(data[i:i+2], 16))
        i += 2
    return result

def hexDecode(cmd):
    return ''.join([ chr(int(cmd[i:i+2], 16)) for i in range(0, len(cmd), 2)])

def hexEncode(string):
    return ''.join(['%02x' % ord(i) for i in string])

