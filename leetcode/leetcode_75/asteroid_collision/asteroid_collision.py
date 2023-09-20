def asteroidCollision1(asteroids: list[int]) -> list[int]:
    st = []
    for a in asteroids:
        if not st:
            st.append(a)
        elif a > 0:
            st.append(a)
        elif st[-1] < 0:
            st.append(a)
        elif st[-1] == -a:
            # st is not empty, a < 0,  st[-1] > 0
            st.pop()
        elif st[-1] > -a:
            pass
        elif st[-1] < -a:
            st.pop()
            while st and 0 < st[-1] < -a:
                st.pop()
            # st is empty or st[-1] < 0 or st[-1] == -a or st[-1] > -a
            if not st or st[-1] < 0:
                st.append(a)
            elif st[-1] == -a:
                st.pop()
            elif st[-1] > -a:
                pass
    return st


def asteroidCollision2(asteroids: list[int]) -> list[int]:
    st = []
    for a in asteroids:
        while st and 0 < st[-1] < -a:
            st.pop()
        if not st or a > 0 or st[-1] < 0:
            st.append(a)
        elif st[-1] == -a:
            st.pop()

    return st


asteroids = [-1, 7, 3,  4, -5]
print(asteroidCollision2(asteroids))
asteroids = [5,10,-5]
print(asteroidCollision2(asteroids))
asteroids = [8,-8]
print(asteroidCollision2(asteroids))
asteroids = [10,2,-5]
print(asteroidCollision2(asteroids))


