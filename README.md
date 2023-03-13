# ZR-APIUtils
ZomsbRoyale.io API utils. Not everything was tested (I'm too lazy) so please report any bugs in my Discord DMs (creaffy#1939). If you know any api endpoints that I didn't include in this project but you think are worth it, also DM me.

## Getting your user key
###
1. Run [Zombs Royale](https://zombsroyale.io/) in your browser and make sure you're logged in
2. Open the console with `Ctrl + Shift + J`
3. Run `console.log(game.options.userData.key);`

That's it. This is your user key.

## Commands
* **.help** -> Commands list
* **.key** -> Edit default userkey
* **.clanlist** -> `/api/clan/available`
* **.joinclan** -> `/api/clan/{0}/join?userKey={1}`
* **.createclan** -> `/api/clan/create?userKey={0}&tag={1}&name={2}&description={3}`
* **.leaveclan** -> `/api/clan/{0}/leave?userKey={1}`
* **.data** -> `/api/user/{0}`
* **.config** -> `/api/config`
* **.clearsessions** -> `/api/user/{0}/clear-sessions`
* **.changeusername** -> `/api/user/{0}/friend-code/update?name={1}`
* **.shop** -> `/api/shop/available`
* **.rewardtracks** -> `api/reward/tracks?userKey={0}`
* **.rewards** -> `api/user/{0}/rewards`
* **.quests** -> `api/quest/available?userKey={0}`
* **.polls** -> `/api/poll/available?userKey={0}`
* **.leaderboards** -> `/api/leaderboard/live?userKey={0}&mode={1}&time={2}&category={3}`

## Q&A
**Q: What are the possible modes for .leaderboards?**</br>
A: solo, duo, squad</br>
**Q: What are the possible time ranges for .leaderboards?**</br>
A: 24h, 7d, 14d, 1m, all *(all time)*</br>
**Q: What are the possible categories for .leaderboards?**</br>
A: kills, kills_per_round, rounds, time_alive, top10, winrate, wins</br>
**Q: Why is your code so bad!!! Why is something not working!!!1111!!**</br>
A: AAAAAAAA UHHHHHHHHH AAHHH report bugs on my discord or in issues
