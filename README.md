# Line Bot Nanami Mami

## 角色介紹
### 七海麻美
![Mami](./img/Mami_profile.jpg)

## Finite State Machine
![fsm](./img/fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"

