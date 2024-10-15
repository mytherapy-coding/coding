   
    
    def encode(self, strs: List[str]) -> str:
        strs += ['']
        escaped_strs = [s.replace('/', '//').replace(':', '/:') for s in strs]
        return ':'.join(escaped_strs)


    def decode(self, s: str) -> List[str]:

        parts = re.split(r'(?<!/):', s)
        
        return [part.replace('/:', ':').replace('//', '/') for part in parts][:-1]