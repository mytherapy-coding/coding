function longestCommonPrefix(strs) {
    if (!strs || strs.length === 0) return "";

    let prefix = strs[0];

    for (let i = 1; i < strs.length; i++) {
        let s = strs[i];

        while (!s.startsWith(prefix)) {
            prefix = prefix.slice(0, -1);
            if (prefix === "") return "";
        }
    }

    return prefix;
}


console.log(longestCommonPrefix(["flower","flow","flight"]));   // "fl"
console.log(longestCommonPrefix(["dog","racecar","car"]));      // ""
console.log(longestCommonPrefix(["interspecies","interstellar","interstate"]));  // "inters"
console.log(longestCommonPrefix(["throne","throne"]));          // "throne"
console.log(longestCommonPrefix(["throne","dungeon"]));         // ""
console.log(longestCommonPrefix(["a"]));                        // "a"
console.log(longestCommonPrefix(["",""]));                      // ""
console.log(longestCommonPrefix(["","abc"]));                   // ""
console.log(longestCommonPrefix(["abc",""]));                   // ""
console.log(longestCommonPrefix(["cir","car"]));                // "c"
