export default interface Coach {
    id: string
    firstName: string
    lastName: string
    areas: string[] | null
    description: string | null
    hourlyRate: number
}