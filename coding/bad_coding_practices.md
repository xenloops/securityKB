# Bad Coding Practices

## WORK IN PROGRESS

These are from the CWE category of the same name ([MITRE link](https://cwe.mitre.org/data/definitions/1006.html)) in a hopefully more convenient format.

*	Class	656	Reliance on Security Through Obscurity (Class)

<details>
  <summary> Comments / formatting </summary>

*	Base	1113	Inappropriate Comment Style
*	Base	1114	Inappropriate Whitespace Style
*	Base	1116	Inaccurate Comments
</details>

<details>
  <summary> Code that shouldn't be there </summary>

*	Base	489	Active Debug Code
*	Base	561	Dead Code
*	Base	1041	Use of Redundant Code
*	Base	1071	Empty Code Block
*	Base	1085	Invokable Control Element with Excessive Volume of Commented-out Code
</details>

<details>
  <summary> Design </summary>

*	Base	1044	Architecture with Number of Horizontal Layers Outside of Expected Range
*	Base	1092	Use of Same Invokable Control Element in Multiple Architectural Layers
</details>

<details>
  <summary> Object-oriented errors </summary>

*	Base	1045	Parent Class with a Virtual Destructor and a Child Class without a Virtual Destructor
*	Base	1063	Creation of Class Instance within a Static Code Block
*	Base	1079	Parent Class without Virtual Destructor Method
*	Base	1082	Class Instance Self Destruction Control Element
*	Base	1087	Class with Virtual Method without a Virtual Destructor

</details>

<details>
  <summary> Variables and constants </summary>

*	Base	547	Use of Hard-coded, Security-relevant Constants
*	Base	562	Return of Stack Variable Address
*	Base	563	Assignment to Variable without Use
*	Base	1046	Creation of Immutable Text Using String Concatenation
*	Base	1099	Inconsistent Naming Conventions for Identifiers
*	Base	1102	Reliance on Machine-Dependent Data Representation
*	Base	1106	Insufficient Use of Symbolic Constants
*	Base	1107	Insufficient Isolation of Symbolic Constant Definitions
*	Base	1108	Excessive Reliance on Global Variables
*	Base	1109	Use of Same Variable for Multiple Purposes
*	Base	1126	Declaration of Variable with Unnecessarily Wide Scope
</details>

<details>
  <summary>  Exception handling </summary>

</details>

<details>
  <summary> Control flow </summary>

*	Base	478	Missing Default Case in Multiple Condition Expression
*	Base	1050	Excessive Platform Resource Consumption within a Loop
</details>

<details>
  <summary> Dependencies  </summary>

*	Base	1103	Use of Platform-Dependent Third Party Components
*	Base	1104	Use of Unmaintained Third Party Components
</details>

<details>
  <summary> Data storage and access </summary>

*	Base	1049	Excessive Data Query Operations in a Large Data Table
*	Base	1067	Excessive Execution of Sequential Searches of Data Resource
*	Base	1072	Data Resource Access without Use of Connection Pooling
*	Base	1073	Non-SQL Invokable Control Element with Excessive Number of Data Resource Accesses
*	Base	1084	Invokable Control Element with Excessive File or Data Access Operations
*	Base	1089	Large Data Table with Excessive Number of Indices
*	Base	1094	Excessive Index Range Scan for a Data Resource
*	Base	1097	Persistent Storable Data Element without Associated Comparison Control Element
*	Base	1098	Data Element containing Pointer Item without Proper Copy Control Element
</details>

<details>
  <summary> Serialization </summary>

*	Base	1066	Missing Serialization Control Element
*	Base	1070	Serializable Data Element Containing non-Serializable Item Elements
</details>

*	Base	358	Improperly Implemented Security Check for Standard
*	Base	360	Trust of System Event Data
*	Base	487	Reliance on Package-level Scope
*	Variant	581	Object Model Violation: Just One of Equals and Hashcode Defined
*	Base	586	Explicit Call to Finalize()
*	Variant	605	Multiple Binds to the Same Port
*	Base	628	Function Call with Incorrectly Specified Arguments
*	Base	654	Reliance on a Single Factor in a Security Decision
*	Base	694	Use of Multiple Resources with Duplicate Identifier
*	Base	807	Reliance on Untrusted Inputs in a Security Decision
*	Base	1043	Data Element Aggregating an Excessively Large Number of Non-Primitive Elements
*	Base	1048	Invokable Control Element with Large Number of Outward Calls
*	Base	1065	Runtime Resource Management Control Element in a Component Built to Run on Application Servers
*	Base	1101	Reliance on Runtime Component in Generated Code
*	Base	1115	Source Code Element without Standard Prologue
*	Base	1117	Callable with Insufficient Behavioral Summary
*	Base	1127	Compilation with Insufficient Warnings or Errors
*	Base	1235	Incorrect Use of Autoboxing and Unboxing for Performance Critical Operations

