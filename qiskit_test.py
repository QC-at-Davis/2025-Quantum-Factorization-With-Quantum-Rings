import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, AncillaRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor
from QuantumRingsLib import JobStatus
from matplotlib import pyplot as plt
import numpy as np
import qiskit

provider = QuantumRingsProvider(token ="rings-128.CvEHATBjdKwjlXLLCRqHPZ1g61HPELRZ", name="jtkeio@ucdavis.edu")
backend = provider.get_backend("scarlet_quantum_rings")
shots = 100

provider.active_account()

shots = 1000
numberofqubits =  int(provider.active_account()["max_qubits"])
q = QuantumRegister(numberofqubits , 'q')
c = ClassicalRegister(numberofqubits , 'c')
qc = QuantumCircuit(q, c)


# Create the GHZ state (Greenberger–Horne–Zeilinger)
qc.h(0);
for i in range (qc.num_qubits - 1):
        qc.cx(i, i + 1);

        # Measure all qubits
        qc.measure_all();

mybackend = QrBackendV2(provider, num_qubits = qc.num_qubits)
qc_transpiled = transpile(qc, mybackend, initial_layout=[i for i in range(0, qc.num_qubits)])
job = mybackend.run(qc_transpiled, shots = shots)

result = job.result()
counts = result.get_counts()
plot_histogram(counts)
