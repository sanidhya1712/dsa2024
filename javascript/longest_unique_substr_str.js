const maxLength =function(string){
    let max =0;
    let start =0;
    const seen = {};
    for(let i=0;i<string.length;i++){
        const char = string[i];        
        // abcbdef
        //  1 3
        if(char in seen){
            start = Math.max(start,seen[char]+1);
        }
        max = Math.max(max,i-start+1);
        //make an entry into hash table if its not there
        seen[char]=i;        
    }
    return max;
}

console.log(maxLength('pqbrstbuvwvxy'));