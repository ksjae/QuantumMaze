from qiskit import(
    QuantumCircuit,
    QuantumRegister,
    ClassicalRegister,
    execute,
    Aer)
simulator = Aer.get_backend('qasm_simulator')

def qrandom():
    qreg_q = QuantumRegister(1, 'q')
    creg_c = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.reset(qreg_q[0])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])
    
    job = execute(circuit,simulator,shots=1)
    result = job.result()
    counts = result.get_counts(circuit)

    lAnswer = [(k[-1],v) for k,v in counts.items()]
    lAnswer.sort(key = lambda x: x[1], reverse=True)
    Y = []
    for k, v in lAnswer: 
        Y.append( [ int(c) for c in k ] )
    return Y[0][0]

if __name__=="__main__":
    print(qrandom())
