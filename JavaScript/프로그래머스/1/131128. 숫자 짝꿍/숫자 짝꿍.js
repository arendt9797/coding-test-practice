function solution(X, Y) {
    const ans = []
    const x = [...X]
    const y = [...Y]
    x.sort((a, b) => a-b)
    y.sort((a, b) => a-b)
    
    while (x.length > 0) {
        const cur = x.pop()
        while (y.length > 0 && y[y.length - 1] > cur) {
            y.pop()
        }
        if (y.length > 0 && y[y.length - 1] === cur) {
            ans.push(cur)
            y.pop()
        }
    }
    if (ans.length === 0) return "-1";
    if (ans.join('') === "0".repeat(ans.length)) return "0";

    return ans.join('');
}