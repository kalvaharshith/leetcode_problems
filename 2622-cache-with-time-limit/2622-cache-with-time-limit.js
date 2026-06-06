var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean}
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const exists =
        this.cache.has(key) &&
        this.cache.get(key).expiry > now;

    this.cache.set(key, {
        value: value,
        expiry: now + duration
    });

    return exists;
};

/** 
 * @param {number} key
 * @return {number}
 */
TimeLimitedCache.prototype.get = function(key) {
    const item = this.cache.get(key);

    if (!item || item.expiry <= Date.now()) {
        return -1;
    }

    return item.value;
};

/** 
 * @return {number}
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (const item of this.cache.values()) {
        if (item.expiry > now) {
            count++;
        }
    }

    return count;
};

/**
 * const obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000)
 * obj.get(1)
 * obj.count()
 */