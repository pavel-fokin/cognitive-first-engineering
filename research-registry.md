# Research Registry

A curated collection of empirical findings that establish the biological constraints underlying Cognitive-First Engineering.

---

## Memory

How information is held, stored, and lost.

### Working Memory Capacity
Humans can hold only ~4 items (chunks) in active focus simultaneously.
— Cowan (2001)

### Working Memory Decay
Without active maintenance, items drop from working memory in 18–30 seconds.
— Peterson & Peterson (1959)

### Long-Term Retention Rate
Only ~2 bits/sec transfer to long-term memory during learning.
— Landauer (1986)

### Forgetting Curve
Without rehearsal, ~70% of information is lost within 24 hours. Exponential decay.
— Ebbinghaus (1885); Murre & Dros (2015)

### Interference
Similar tasks (overlapping context, naming) overwrite each other in memory, accelerating forgetting.
— Baddeley & Hitch (1974); Wickens (1963)

---

## Attention

How focus is sustained, divided, and disrupted.

### Context Switching Cost
Full focus recovery after an interruption takes ~23 minutes on average.
— Mark (2008)

### Micro-Interruption Effect
A 2.8-second interruption doubles error rate on the current task.
— Altmann, Trafton & Hambrick (2014)

### Attention Residue
Rapid task-switching leaves cognitive resources "stuck" on the previous task, reducing effective capacity.
— Leroy (2009)

### Multitasking Penalty
Parallel cognitive tasks reduce productivity by 40% and cause an IQ drop of 10–15 points.
— Rubinstein, Meyer & Evans (2001)

### Vigilance Decrement
Sustained attention degrades after 20–30 minutes. Ultradian rhythms cap deep work at ~90-minute blocks.
— Mackworth (1948); Kleitman (1963)

### Anticipation Effect
Expecting an interruption (e.g., on-call) reduces working memory by ~20%, blocking flow state.
— Mellner (2016)

### Brain Drain Effect
The mere presence of a smartphone reduces available working memory—even when it's off.
— Ward et al. (2017)

---

## Communication

How information transfers between people.

### Conscious Throughput
Maximum conscious processing speed: 10–60 bits/sec. Sensory input: ~11 Mbit/sec.
— Zheng & Meister (2024); Nørretranders (1998)

### Speech Information Rate
Verbal information transfer is capped at ~39 bits/sec across all human languages.
— Pellegrino et al. (2011)

### Cost of Grounding
In complex dialogues, up to 50% of time is spent confirming mutual understanding, not transmitting content.
— Clark (1996)

### The Vocabulary Problem
Probability that two experts name the same function with the same word: <20%.
— Furnas et al. (1987)

### Illusion of Transparency
We overestimate how well others understand us. "Tappers & Listeners": expected 50% comprehension, actual 2.5%.
— Newton (1990)

### Neural Coupling
Understanding requires physical synchronization of brain activity between speaker and listener. Model mismatch breaks the link.
— Stephens et al. (2010)

---

## Decision and Planning

How choices are made and tasks are managed.

### Bounded Rationality
Humans decide using simplified models, not complete information, due to resource constraints.
— Simon

### Hick's Law
Decision time grows logarithmically with the number of options.
— Hick (1952)

### Decision Fatigue
The capacity to make choices is a depletable resource. Long backlogs exhaust it.
— Baumeister et al. (1998)

### Zeigarnik Effect
Incomplete tasks consume cognitive resources. Creating a concrete plan releases them.
— Masicampo & Baumeister (2011)

---

## Comprehension

How systems and situations are understood.

### Cognitive Load Theory
Distinguish *intrinsic* load (task essence) from *extraneous* load (poor presentation). Minimize the latter.
— Sweller (1988)

### Free Energy Principle
The brain minimizes "surprise" (prediction error). Predictable systems reduce metabolic cost.
— Friston

### Situation Awareness
Three levels of system understanding: perception → comprehension → projection.
— Endsley (1995)

### Distributed Cognition
Thinking happens not in the head alone, but across the system of Human + Tools.
— Hutchins

---

## Coordination

How groups organize and collaborate.

### Dunbar's Number
Stable social relationships cap at ~150; effective team size is 5–9.
— Dunbar

---

## How to Use This Registry

Each entry establishes a **constraint**—a limit that exists regardless of methodology, tooling, or intent. When designing systems, processes, or architectures, these findings define the boundaries of what humans can reliably perceive, remember, process, and coordinate.

Use these constraints as design inputs, not afterthoughts. When a system violates a limit, expect failure—not through lack of effort, but through physics.

---

## Contributing

To add research to this registry:
1. Ensure the finding is empirically grounded (peer-reviewed or replicated).
2. Express the insight as a constraint or limit, not a recommendation.
3. Include a primary reference.
