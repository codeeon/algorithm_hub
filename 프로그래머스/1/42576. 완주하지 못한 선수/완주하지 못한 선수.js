function solution(participant, completion) {
    const people = {}

    participant.forEach(name => people[name] ? people[name] += 1 : people[name] = 1)
    
    completion.forEach(name => {
        if (people[name] !== undefined) {
            people[name] -= 1
        } else {
            return name
        }
    })

    for (const key in people) {
        if (people[key] === 1) return key
    }
}