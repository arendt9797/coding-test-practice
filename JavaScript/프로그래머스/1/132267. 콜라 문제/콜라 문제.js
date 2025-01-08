function solution(a, b, n) {
    let bottle = 0
    function getBottle(give, get, cur) {
        if (cur < give) {
            return
        }
        let quota = parseInt(cur/give)
        let res = cur%give
        let newBottle = quota*get
        
        bottle += newBottle
        getBottle(give, get, newBottle+res)
    }
    getBottle(a, b, n)
    return bottle
}